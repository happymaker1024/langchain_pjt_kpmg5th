# streamlit run main_app.py
import streamlit as st
from report_service import investment_report
from search_index import SearchResult, search_compay
from stock_info import Stock

st.title("AI 투자 보고서 생성 서비스")
# search_query = st.text_input("회사명", "Apple Inc")
# company_list = ["AAPL: Apple Inc",
#                 "APLE: Apple Hospitality REIT Inc"]
# company_selected = st.selectbox("회사 선택", company_list, index=0)

# 회사 이름, symbol
# compay = "Apple Inc"
# symbol = "AAPL"

search_query = st.text_input("회사명","Apple Inc")
# 서치 목록 만들기
hits = search_compay(search_query)['hits']  # hits 키로 데이터 목록이 만들어져 있음
search_results = [SearchResult(hit) for hit in hits]
# Symbol, Name 추출
company_selected = st.selectbox("회사 선택", search_results)

# tab으로 구분해서 보기
tabs = ["주식 정보", "투자 보고서"]
tab1, tab2 = st.tabs(tabs)

# 주식 거래량 시각화
with tab1:
    st.header(f"{search_query}의 6개월 주식 거래량")
    stock = Stock(company_selected.symbol)
    volume = stock.get_stock_volume()
    st.line_chart(volume, use_container_width=True)

with tab2:
    st.header(f"{search_query} 투자보고서 생성")

    if st.button("투자 보고서 생성"):
        with st.spinner(text="투자 보고서 생성 중..."):
            report = investment_report(company_selected.name, company_selected.symbol)
            st.success("투자 보고서 생성 완료!")            
        st.write(report)