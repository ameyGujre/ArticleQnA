import streamlit as st
from utils import create_embeddings

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
    
if st.session_state.authenticated:
    st.title("Update new article")
    url = st.text_input(label="Enter the web URL to update the article into the database:")
    if st.button("Upload"):
        with st.spinner("Pushing into the database"):
            response = create_embeddings(url)
            if response:
                st.success("Article updated into database, and ready for QnA")
            else:
                st.warning(f"The process got broken with the error: {response}")
    
    
else:
    st.write("Enter Admin AuthKey")
    text = st.text_input(label="Authkey", type='password')
    if st.button(label="Submit"):
        if str(text) == "root":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Unauthorized")
