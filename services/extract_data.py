import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def extract_data(ExtractionData, invoke_prompt, chat_prompt, file_path, search_type="similarity"):

    loader = PyPDFLoader(file_path)
    documents = loader.load()
    vectorstore = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings())

    if search_type == "similarity":
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 30})
    else:
        retriever = vectorstore.as_retriever(search_type="mmr")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                chat_prompt,
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