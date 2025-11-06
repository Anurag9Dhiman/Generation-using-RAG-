# Generation-using-RAG-
An Object-Oriented Retrieval-Augmented Generation (RAG) system that uses academic assignments as a knowledge base to generate accurate, context-aware solutions using open-source NLP tools.

# Assignment RAG Project

Open-source RAG (Retrieval-Augmented Generation) project that uses assignment materials as a local knowledge base. Uses embeddings + Chroma (vector DB) for retrieval and a Hugging Face model for generation.

## Features

- 📚 Processes Jupyter notebooks (`.ipynb`) and Python scripts (`.py`) from your assignments
- 🔍 Semantic search using sentence-transformers embeddings
- 💾 Local vector database with ChromaDB (persistent storage)
- 🤖 Text generation using Hugging Face transformers
- 🔒 Fully local execution - no external APIs required

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd assignment_rag_project
```

### 2. Create a Python virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# .\.venv\Scripts\activate  # Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Add your assignment files

Place your assignment files (`.ipynb` or `.py`) in the `data/` folder.

### 5. Build the vector database

```bash
python build_db.py
```

This will:
- Preprocess files from `data/` → `processed_data/`
- Split texts into chunks
- Create embeddings and store them in `vector_db/`

### 6. Run the app

```bash
python main.py
```

Type your questions and press Enter. Type `exit` to quit.

## Project Structure

```
assignment_rag_project/
├── data/                  # Input: Your assignment files (.ipynb, .py)
├── processed_data/        # Intermediate: Preprocessed text files
├── vector_db/            # Vector database storage (ChromaDB)
├── modules/              # Core modules
│   ├── database.py       # Vector database & embeddings
│   ├── preprocessor.py   # File preprocessing
│   ├── retriever.py      # Document retrieval
│   ├── generator.py      # Text generation
│   └── pipeline.py       # RAG pipeline orchestration
├── utils/                # Utilities
│   └── text_splitter.py  # Text chunking
├── build_db.py           # Build vector database script
├── main.py               # Main application entry point
└── requirements.txt      # Python dependencies
```

## Technology Stack

- **Embeddings**: `sentence-transformers` (all-MiniLM-L6-v2)
- **Vector DB**: `chromadb` (local persistence)
- **Generation**: `transformers` (distilgpt2 by default)
- **Text Processing**: `nbformat` for Jupyter notebooks

## Configuration

- **Embedding Model**: Change in `modules/database.py` (default: `all-MiniLM-L6-v2`)
- **Generator Model**: Change in `modules/generator.py` (default: `distilgpt2`)
- **Retrieval Top-K**: Adjust in `modules/retriever.py` (default: 3)

## Notes

- First run will download models from Hugging Face (requires internet)
- All data processing happens locally - your files never leave your machine
- You can swap models as needed - just update the model names in the respective modules

## License

Open-source project - feel free to modify and extend as needed.



