from modules.retriever import Retriever
from modules.generator import Generator


class RAGPipeline:
    def __init__(self, db):
        self.retriever = Retriever(db)
        self.generator = Generator()


    def run(self, query):
        docs = self.retriever.retrieve(query)
        context = '\n'.join(docs)
        return self.generator.generate(query, context)