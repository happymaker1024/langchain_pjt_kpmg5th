# streamlit run main_app.py
import streamlit as st
from report_service import investment_report

st.title("AI 투자 보고서 생성 서비스")
st.text_input("회사명", "Apple Inc")
company_name = ["AAPL: Apple Inc",
                "APLE: Apple Hospitality REIT Inc"]
company = st.selectbox("회사 선택", company_name, index=0)


# 회사 이름, symbol
compay = "Apple Inc"
symbol = "AAPL"
st.header(f"{company} 투자보고서 생성")

if st.button("투자 보고서 생성"):
    with st.spinner(text="투자 보고서 생성 중..."):
        report = investment_report(compay, symbol)
        st.success("투자 보고서 생성 완료!")
        st.markdown(report, unsafe_allow_html=True)
    st.write(report)