from langchain_community.vectorstores import Chroma

client = chromadb.PersistentClient(path="./db")
#col = client.get_collection(name="recipe")
print(len(client.list_collections()))

#print(len(col))
