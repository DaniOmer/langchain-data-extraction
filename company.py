import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from schema.Company.Company import ExtractionData as CompanySchema
from services.company.company import get_company_data

llm = ChatOpenAI(model="gpt-4o-mini", temperature=1)

def extract_data(ExtractionData, invoke_prompt, file_path):

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    vectorstore = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 30})
    # retriever = vectorstore.as_retriever(search_type="mmr")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert at identifying key information about the company in the text."
            ),
            ("human", "{text}"),
        ]
    )

    extractor = prompt | llm.with_structured_output(
        schema=ExtractionData,
        include_raw=False,
    )

    rag_extractor = {
        "text": retriever | (lambda docs: docs)
    } | extractor

    results = rag_extractor.invoke(invoke_prompt)

    return results

def handler(event):
    company_name = event['company_name']
    file_path = (
        event['file_path']
    )

    output_path = f"data/{company_name}/Company/company.json"
    invoke_prompt = "Key informations associated to the company."

    data = extract_data(CompanySchema, invoke_prompt, file_path)
    get_company_data(data, output_path)


event = {
    'file_path' : './filings/ABBOTT-LABORATORIES-DEF-14-PROXY.pdf',
    'company_name': "ABBOTT-LABORATORIES"
}

handler(event)

