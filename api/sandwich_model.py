import chromadb
import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

MODEL = "llama3"
OPENAI_KEY = os.getenv("OPENAI_KEY")
DB_PATH = os.getenv("DB_PATH") or "./db"

class SandwichModel:
    def __init__(self, name):
        self.sandwich_name = name
        self.db = self._get_database_connection()
        self.model = Ollama(model=MODEL)

    def generate_sides(self):
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=self._default_prompt(),
        )

        chain = RetrievalQA.from_chain_type(
            self.model,
            retriever=self.db.as_retriever(),
            chain_type_kwargs={"prompt": prompt}
        )

        query = f"What is a good side-dish for a {self.sandwich_name}"

        try:
            return chain.invoke({"query": query})["result"]
        except:
            return "Error generating an answer"

    def _get_database_connection(self):
        client = chromadb.PersistentClient(path=DB_PATH)
        return Chroma(
            client=client,
            collection_name="recipes",
            embedding_function=OpenAIEmbeddings(api_key=OPENAI_KEY),
            persist_directory=DB_PATH
        )

    def _default_prompt(self):
        return """
INSTRUCTIONS
Answer the QUESTION using the recipes in the book text above
You are a culinary assistant, your task is to provide recipes for side dishes from this book
Include the list of ingredients, step-by-step instructions, and any tips or variations mentioned in the book
Statements like "according to the book" or similar in your answers should be avoided, skip referencing book in general
Use the following recipes to answer the question to the best of your capacity:
{context}

QUESTION
{question}
"""
