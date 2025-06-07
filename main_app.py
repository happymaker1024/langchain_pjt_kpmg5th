# streamlit run main_app.py
import streamlit as st
from report_service import investment_report

st.title("AI 투자 보고서 생성 서비스")
st.text_input("회사명", "Apple Inc")
company_list = ["AAPL: Apple Inc",
                "APLE: Apple Hospitality REIT Inc"]
company_selected = st.selectbox("회사 선택", company_list, index=0)


# 회사 이름, symbol
compay = "Apple Inc"
symbol = "AAPL"

# tab으로 구분해서 보기
tabs = ["주식 정보", "투자 보고서"]
tab1, tab2 = st.tabs(tabs)

# 주식 거래량 시각화
with tab1:
    st.header(f"{compay} 주식 정보")
    st.text("주식 거래량 시각화는 아직 구현되지 않았습니다.")
    # 여기에 주식 거래량 시각화 코드를 추가할 수 있습니다.

with tab2:
    st.header(f"{compay} 투자보고서 생성")

    if st.button("투자 보고서 생성"):
        with st.spinner(text="투자 보고서 생성 중..."):
            report = investment_report(compay, symbol)
            st.success("투자 보고서 생성 완료!")            
        st.write(report)