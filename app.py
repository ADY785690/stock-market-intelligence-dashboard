import streamlit as st

st.set_page_config(page_title="Stock Market Intelligence Dashboard")

st.title("📈 Stock Market Intelligence Dashboard")

st.write("""
This project analyzes stock performance using Python and Yahoo Finance.
It includes stock return analysis, volatility analysis, portfolio simulation,
moving averages, and NIFTY 50 benchmark comparison.
""")

st.header("Stocks Analyzed")

st.write("""
- Reliance Industries
- Tata Consultancy Services (TCS)
- Infosys
- HDFC Bank
""")

st.header("Project Features")

st.write("""
✅ Single Stock Analysis

✅ Multi Stock Comparison

✅ Daily Return Analysis

✅ Volatility Analysis

✅ Portfolio Simulation

✅ 50-Day Moving Average Analysis

✅ NIFTY 50 Benchmark Comparison
""")

st.header("Key Findings")

st.write("""
- Infosys showed the highest volatility.
- HDFC Bank was the most stable stock.
- Reliance generated the highest return.
- Diversification helps reduce investment risk.
""")

st.header("Project Output")

st.image("reliance_stock_analysis.png",
         caption="Reliance Stock Analysis")
