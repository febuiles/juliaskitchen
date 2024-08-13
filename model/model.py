import chromadb
import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

db = chromadb.PersistentClient(path="../db")
vectorstore = Chroma(
    client=db,
    collection_name="recipes",
    embedding_function=OpenAIEmbeddings(api_key=os.getenv("OPENAI_KEY")),
    persist_directory="../db"
)

template = """book:
{context}

QUESTION
{question}

INSTRUCTIONS
Answer the QUESTION using the recipes in the book text above
You are a culinary assistant, your task is to provide recipes for side dishes from this book
Include the list of ingredients, step-by-step instructions, and any tips or variations mentioned in the book
Statements like "according to the book" or similar in your answers should be avoided, skip referencing book in general
"""

query_text = "What is a good side dish or salad for a cheese sandwich?"

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template,
)

model = Ollama(model="llama3")

chain = RetrievalQA.from_chain_type(
    model,
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": prompt},
)

print(chain.invoke({"query": query_text}))
