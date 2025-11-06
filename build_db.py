import os
from modules.preprocessor import AssignmentPreprocessor
from modules.database import VectorDatabase
from utils.text_splitter import split_text


def main():
    pre = AssignmentPreprocessor()
    pre.process_all()


    db = VectorDatabase()


    docs = []
    for file in os.listdir('processed_data'):
        with open(os.path.join('processed_data', file), 'r', encoding='utf-8') as f:
            text = f.read()
        chunks = split_text(text)
        docs.extend(chunks)


    db.add_documents(docs)
    print('✅ Vector database built successfully.')


if __name__ == '__main__':
    main()