import streamlit as st
from chatFile import *

start = 0
st.header('Welcome to Legendary GPT')
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    name = st.text_area(label="Your Name")

key = "sk-proj-dneCSt7nykbPyGV8Nw5MT3BlbkFJ4vZxeWMfYKJsnX6B6RNo"

url = st.text_area(label="Enter URL.....")


temperature = st.slider("Creativity", 0,10,5)

if st.button("Process"):
        with st.spinner():
            openaiKey(key)
            web(url)
            chat_connection()
            print("done")

query = st.text_area(label="Your Query")
try:
    if st.button("Enter"):
            st.markdown("### Result From Legendary GPT")
            print("done1")
            ans = chatnew(query)
            st.write(ans)
except:
    st.write("First Enter Details and Process")
