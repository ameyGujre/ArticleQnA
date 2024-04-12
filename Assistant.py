import streamlit as st
from utils import get_response
st.title("Article QnA Assistant")
st.caption("This is a QnA Assistant powered by gpt3.5turbo")


prompt = st.chat_input("Enter your query")



if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.spinner("Processing your query"):
        response = get_response(prompt)
        
        with st.chat_message("assistant"):
            st.write(response)