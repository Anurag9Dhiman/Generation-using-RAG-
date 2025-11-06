class Retriever:
    def __init__(self, db):
        self.db = db


    def retrieve(self, query, top_k=3):
        return self.db.query(query, top_k=top_k)