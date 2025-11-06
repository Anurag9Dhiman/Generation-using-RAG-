from modules.database import VectorDatabase
from modules.pipeline import RAGPipeline


if __name__ == '__main__':
    db = VectorDatabase()
    rag = RAGPipeline(db)


    print('🔍 RAG System Ready. Type a question (or "exit" to quit).')
    while True:
        query = input('\n🧠 Query: ')
        if query.lower() == 'exit':
            break
        answer = rag.run(query)
        print(f'\n💡 Answer:\n{answer}\n')