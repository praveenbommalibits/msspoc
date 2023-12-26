import streamlit as st
def main():
    st.set_page_config("Chat with Multiple PDFs", page_icon=":books:")
    st.header("Chat with Multiple PDFs :books:")
    with st.sidebar:
        st.header("MSS")
        st.title("LLM Chatapp using LangChain")
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload the PDF Files here and Click on Process", accept_multiple_files=True)
        st.button("Process")

        st.markdown('''
        - [Streamlit](https://streamlit.io/)
        - [LangChain](https://python.langchain.com/)
        - [OpenAI](https://platform.openai.com/docs/models) LLM Model
        ''')
        st.write('Sample text here ')
if __name__ == "__main__":
    main()