import os, chromadb
from sentence_transformers import SentenceTransformer


class VectorDatabase:
    def __init__(self, persist_dir='vector_db'):
        os.makedirs(persist_dir, exist_ok=True)
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection('assignments')
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')


    def add_documents(self, docs):
        embeddings = self.embedder.encode(docs)
        ids = [f'doc_{i}' for i in range(len(docs))]
        self.collection.add(documents=docs, embeddings=embeddings, ids=ids)


    def query(self, text, top_k=3):
        emb = self.embedder.encode([text])
        results = self.collection.query(query_embeddings=emb, n_results=top_k)
        return results['documents'][0]