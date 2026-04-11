import streamlit as st

st.title("🎉 我的第一个个人网站")
st.write("你好！这是我用 Python 做的网站！")

name = st.text_input("熊熊")
if name:
    st.success(f"欢迎你，{name}！")
