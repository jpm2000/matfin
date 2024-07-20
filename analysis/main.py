import os
import pandas as pd
from pandasai import Agent
from pandasai import SmartDatalake
from pandasai.llm import AzureOpenAI
import insert_documents as doc
from insert_documents import select_excel_file, create_dataframe_from_excel


if __name__ == "__main__":
    file_path = select_excel_file()
    if not file_path:
        print("No file selected.")
        exit()

    df = create_dataframe_from_excel(file_path)
    if df is None:
        print("DataFrame creation failed.")
        exit()


    api_token = "129b955551864d868384a4e3fa6ceb68"
    azure_endpoint = ("https://azureai-instance077170078549.openai.azure.com/")
    api_version = "2024-02-15-preview"  # Update this if necessary
    deployment_name = 'gpt-4'  # Ensure this matches your deployment

    llm = AzureOpenAI(
        api_token=api_token,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
        deployment_name=deployment_name
    )

    agent = Agent(df, config={"llm": llm})
    prompt = input('Write down your query: ')
    result = agent.chat(prompt)
    print(result)

