
# Import os to set API key
import os
# Import OpenAI as main LLM service
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
# Bring in streamlit for UI/app interface
import streamlit as st
# from PIL import Image

# Import PDF document loaders...there's other ones as well!
from langchain.document_loaders import PyPDFLoader
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
llm = OpenAI(temperature=0, verbose=True)
embeddings = OpenAIEmbeddings()

# Create and load PDF Loader
loader = PyPDFLoader('annualreport.pdf')
# Split pages from pdf 
pages = loader.load_and_split()
# Load documents into vector database aka ChromaDB
store = Chroma.from_documents(pages, embeddings, collection_name='annualreport')

# Create vectorstore info object - metadata repo?
vectorstore_info = VectorStoreInfo(
    name="annual_report",
    description="a annual report for a big company",
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

st.title('Bucks DEMO 🟩')    
# App Create a text input box for the user
prompt = st.text_input('Write your prompy here')

# App Footer
st.link_button('Financial statements','https://docs.google.com/spreadsheets/d/102s5ZUT-sfZafSamdopOYO0sJ-D_it8w/edit?usp=sharing&ouid=116985559880734756081&rtpof=true&sd=true')

st.info('This is a trial version of Bucks financial assistant')




# Prompt template
data_template = PromptTemplate(
    input_variables= ['data'],
    # act like a financial expert based on the file annualreport.pdf to respond:
    template='based on the file annualreport.pdf respond: {data}'
)
analysis_template = PromptTemplate(
    input_variables= ['analysis'],
    #based on the data from annualreport.pdf provide a financial analysis and key metrics
    template='provide further financial information {analysis}'
)

# LLM
data_chain = LLMChain(llm=llm, prompt=data_template, verbose=True, output_key='analysis')
analysis_chain = LLMChain(llm=llm, prompt=analysis_template, verbose=True, output_key='script')
sequential_chain = SequentialChain(chains=[data_chain, analysis_chain], input_variables=['data'], output_variables=['analysis', 'script'], verbose=True)

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = sequential_chain({'data':prompt})
    # ...and write it out to the screen
    st.write(response['analysis'])
    st.write(response['script'])
    # st.write(response)

    # With a streamlit expander  
    with st.expander('Document Search'):
        # Find the relevant pages
        search = store.similarity_search_with_score(prompt) 
        # Write out the first 
        st.write(search[0][0].page_content) 