
# Import os to set API key
import os
# Import OpenAI as main LLM service
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
# Bring in streamlit for UI/app interface
import streamlit as st
# from PIL import Image

# Import PDF document loaders...there's other ones as well!
from langchain.document_loaders import PyPDFLoader, OnlinePDFLoader
# Import chroma as the vector store 
from langchain.vectorstores import Chroma
# Import prompt templates
from langchain.prompts import PromptTemplate
# Import llm chain
from langchain.chains import LLMChain, SequentialChain

# Import openai
import openai

# Import vector store stuff
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# Set APIkey for OpenAI Service
# Can sub this out for other LLM providers
openai.api_key = os.environ['OPENAI_API_KEY']


# Create instance of OpenAI LLM
llm = OpenAI(temperature=2, verbose=True)
embeddings = OpenAIEmbeddings()

# Upload file
file = st.file_uploader("Upload a CSV file", type='pdf')

if file is not None:
    temp_path = f"/Users/juanmanrique/Documents/matfin/{file.name}"  # Assuming 'temp' is a directory for temporary files
    with open(temp_path, 'wb') as temp_file:
        temp_file.write(file.read())

    # Create and load PDF Loader
    # path = OnlinePDFLoader(temp_path)
    loader = PyPDFLoader(temp_path)

    # Split pages from PDF
    pages = loader.load_and_split()
    # pages = loader.split(pdf_content)
    
    # Load documents into vector database aka ChromaDB
    store = Chroma.from_documents(pages, embeddings, collection_name='pdf_file')
    
    
    # Create vectorstore info object - metadata repo?
    vectorstore_info = VectorStoreInfo(
        name="pdf_file",
        description="a pdf file with financial information",
        vectorstore=store
    )
    # Convert the document store into a langchain toolkit
    toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

    # Add the toolkit to an end-to-end LC
    agent_executor = create_vectorstore_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )

# App Header
#col1, col2 = st.columns(2)

#with col1:
    #st.image('logo.png', width=100, output_format='PNG')

st.link_button('Web site','https://www.bucks-finance.com/es')

st.title('Bucks PDF')    
# App Create a text input box for the user
prompt = st.text_input('Write your prompy here')

# App Footer
st.info('This is a trial version of Bucks financial assistant')

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = agent_executor.run(prompt)
    # ...and write it out to the screen
    st.write(response)

    # With a streamlit expander  
    with st.expander('Document Similarity Search'):
        # Find the relevant pages
        search = store.similarity_search_with_score(prompt) 
        # Write out the first 
        st.write(search[0][0].page_content) 
        

    os.remove(temp_path)