import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from schema.Executive.ExecutiveCompensation import ExtractionData as ExecutiveExtrationSchema
from schema.Mandatary.MandataryCompensation import ExtractionData as MandatoryExtractionSchema
from services.executive.executive_compensation import get_executive_compensations
from services.mandatary.mandatary_compensation import get_mandatary_compensations

llm = ChatOpenAI(model="gpt-4o-mini", temperature=1)
# llm = ChatOpenAI(model="gpt-4-0125-preview", temperature=1)
# llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

def extract_data(ExtractionData, invoke_prompt, file_path):

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    vectorstore = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings())
    # retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 30})
    retriever = vectorstore.as_retriever(search_type="mmr")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert at identifying key information about the company and his members in the text."
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
    role = event['role']
    file_path = (
        event['file_path']
    )

    executive_output_path = f"data/{company_name}/{role}/Compensation/compensation.json"
    mandatary_output_path = f"data/{company_name}/{role}/Compensation/compensation.json"

    invoke_prompt_for_executive = "Key informations associated with executive officers."
    invoke_prompt_for_mandatary = "Key informations associated with non-employee directors also known as board committees."

    if role == 'Mandatary':
        mandatary_compensation_data = extract_data(MandatoryExtractionSchema, invoke_prompt_for_mandatary, file_path)
        get_mandatary_compensations(mandatary_compensation_data, mandatary_output_path)
    elif role == 'Comex':
        executive_compensations_data = extract_data(ExecutiveExtrationSchema, invoke_prompt_for_executive, file_path)
        get_executive_compensations(executive_compensations_data, executive_output_path)

event = {
    'file_path' : './filings/ABBOTT-LABORATORIES-DEF-14-PROXY.pdf',
    'role' : 'Mandatary',
    'company_name': "ABBOTT-LABORATORIES"
}

handler(event)

