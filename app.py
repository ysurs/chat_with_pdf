import streamlit as st
from dotenv import load_dotenv


def main():
    
    load_dotenv()
    st.set_page_config(page_title="chat with pdfs",page_icon=":books:")
    
    st.header("Chat with muliple pdfs :books:")
    st.text_input("Ask any question about your pdfs")
    
    with st.sidebar:
     st.subheader("Your documents")
     st.file_uploader("Upload your pdfs here and click on 'Process'")
     st.button("Process")
     

if __name__ == '__main__':
    main()
    