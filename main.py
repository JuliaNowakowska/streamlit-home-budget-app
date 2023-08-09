import streamlit as st

st.write("""
# Home Budget app
""")

categories = ["food", "flat"]

col1, col2 = st.columns(2)

with col1:
    st.number_input("How much did you spend?", step=0.1)
    st.text_input("Name of the shop:")

with col2:
    st.selectbox("Category: ", categories)
    st.date_input("When?")


