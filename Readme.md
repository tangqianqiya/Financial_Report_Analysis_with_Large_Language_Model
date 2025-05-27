# 🚀 Financial Report Analysis with Large Language Model

## 📌 Overview
The **Financial Report Analysis with Large Language Model** is an AI-powered system that leverages **Retrieval-Augmented Generation (RAG)** to analyze and extract valuable insights from financial reports. It integrates **Large Language Models (LLMs)**, **vector databases**, and **NLP techniques** to provide **accurate, real-time** financial knowledge retrieval and analysis.

This system runs locally using the DeepSeek R1 model, powered by Ollama or vLLM for efficient on-device execution. With a Streamlit-based GUI I wrote from scratch, it enables seamless financial report analysis while ensuring data privacy. Because the model operates entirely offline, it is ideal for highly confidential environments, such as organizations and individuals who prefer to keep their financial data secure and independent from cloud providers.


## ✨ Features
- 📊 **AI-powered Financial Report Analysis** - Uses LLMs to process and extract key financial insights.
- 🔍 **Vector Database Integration** - Efficient retrieval of financial documents.
- 📈 **NLP-driven Sentiment Analysis** - Extracts market sentiment from financial texts.
- 🤖 **Chatbot for Financial Q&A** - Answers financial-related queries with up-to-date information.
- 📂 **Document Processing Pipeline** - Converts raw financial documents into structured formats.
- ⚡ **Fast and Scalable** - Built with **LangChain** for real-time financial analysis with RAG.

## 📂 Project Structure
```
Financial_Reports_Analyzer_RAG_with_DeepSeek_R1/
│── README.md
│── requirements.txt
│── setup.py
│── financial_rag/
│   │── main.py
│   │── configure.py
│   │── .env
│   │── backend/
│   │   │── __init__.py
│   │   │── chatbot.py
│   │   │── document_processor.py
│   │   │── vector_db.py
│   │── data/
│   │   │── chroma_db/
│   │   │── embeddings/
│   │   │── uploaded_pdfs/
│   │── models/
│   │   │── __init__.py
│   │   │── models.py
│   │── utils/
│   │   │── __init__.py
│   │   │── logger.py
│   │   │── search_engine.py
```

## 🔧 Installation
### 1️⃣ **Clone the repository**
```sh
git clone https://github.com/EasonJia9598/financial_rag.git
cd financial_rag
```

### 2️⃣ **Create a virtual environment**
```sh
conda create --name myenv python=3.12
conda activate myenv
```

### 3️⃣ **Install dependencies**
```sh
conda install -r requirements.txt
```

### 4️⃣ **Set up environment variables**
Create a `.env` file in the root directory and configure:
```
CHROMA_DB_PATH = "financial_rag/data/chroma_db"
EMBED_MODEL_NAME = 'all-MiniLM-L6-v2'
LLM_MODEL = "deepseek-r1:14b"
EXPERT_PROMPT_PATH = "financial_rag/Expert_Prompt"
```

### 5️⃣ **Run the application**
```sh
streamlit run ./financial_rag/main.py
```

## 🏗️ Technologies Used
- **Python** 🐍
- **DeepSeek R1** 🤖
- **ChromaDB** 📊
- **LangChain** 🧠
- **FAISS** 🔍
- **Selenium** 🌐
- **Pandas & NumPy** 📊
- **Matplotlib & Seaborn** 📈
