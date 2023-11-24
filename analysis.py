# Import libraries
import os
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
import pandas as pd

# Import openai
import openai

# Import vector store stuff
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

financial_sample = pd.read_csv('/Users/juanmanrique/Documents/matfin/financial_sample.csv', sep=',', header=0)
print(financial_sample)

amazon_csv = pd.read_csv('/Users/juanmanrique/Documents/matfin/amazon-2.csv', sep=',', header=0)

os.getenv("OPENAI_API_KEY") == os.environ['OPENAI_API_KEY']

agent = create_csv_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    financial_sample,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

agent.run("how many rows are there?")
