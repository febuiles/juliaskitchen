import logging
import os

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

logging.basicConfig(level="INFO")

loader = TextLoader("book.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

client = Chroma.from_documents(
    documents=texts,
    embedding=OpenAIEmbeddings(api_key=os.getenv("OPENAI_KEY")),
    collection_name="recipes",
    persist_directory="../db/"
)

logging.info(f'Recipe collection now has {client._collection.count()} embeddings')
