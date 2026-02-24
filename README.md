# 🎬 YouTube Video RAG ChatBot Project

An AI-driven chatbot that allows users to **ask questions about any YouTube video** and receive accurate answers based on the video’s content using **Retrieval-Augmented Generation (RAG)** with LangChain and vector embeddings.

---

## 🧠 About

This project extracts transcripts from YouTube videos, transforms them into embeddings stored in a vector database, and builds an intelligent chatbot that can:

- ✔ Understand video content  
- ✔ Answer user questions with context-aware responses  
- ✔ Provide summaries, explanations, and detailed insights from videos  

Instead of directly passing the entire transcript to an LLM, this system uses **RAG (Retrieval-Augmented Generation)** to retrieve only the most relevant chunks before generating answers.  
This improves accuracy, reduces hallucinations, and ensures responses are grounded in the actual video content.

---

## 🚀 Features

- ✔ Fetch YouTube video transcripts  
- ✔ Convert transcript text into embeddings  
- ✔ Store embeddings for efficient retrieval  
- ✔ Perform semantic search over video content  
- ✔ Generate context-aware responses  
- ✔ Interactive Streamlit-based chat interface  

---

## 🧱 Tech Stack

- **Python**
- **LangChain**
- **HuggingFace / LLM API**
- **FAISS / Chroma (Vector Database)**
- **YouTube Transcript Fetching**
- **Streamlit (User Interface)**

---

## 🛠 How It Works

1. User enters a YouTube video URL.
2. The transcript is fetched automatically.
3. The transcript is split into smaller chunks.
4. Each chunk is converted into vector embeddings.
5. Embeddings are stored in a vector database.
6. The user asks a question.
7. Relevant chunks are retrieved using semantic similarity search.
8. The LLM generates a context-aware response using retrieved data.

---

## 🧪 Example Use Cases

- “What are the key points explained in the video?”
- “Summarize the speaker’s recommendations.”
- “What tool did the presenter mention at minute 8:45?”
- “Explain the concept of X from the video.”

---

## 🤔 Why LangChain Instead of LangGraph?

In this project, **LangChain** was used instead of **LangGraph** because the application follows a **straightforward RAG pipeline** and does not require complex agent workflows.

---

### ✅ Why LangChain Was Chosen

This project involves:

- Loading YouTube transcripts  
- Splitting text into chunks  
- Creating embeddings  
- Storing them in a vector database  
- Retrieving relevant context  
- Generating responses using an LLM  

This is a **linear and well-defined workflow**, which LangChain handles efficiently using:

- Document Loaders  
- Text Splitters  
- Embedding Models  
- Vector Stores  
- Retrievers  
- LLM Chains  

LangChain provides all the required abstractions for building a modular and scalable RAG system without unnecessary orchestration complexity.

---

### 🧠 Why LangGraph Was Not Used

LangGraph is more suitable for:

- Multi-agent systems  
- Complex branching logic  
- Stateful workflows  
- Tool-calling agents with decision loops  
- Advanced conversational memory management  

Since this project:

- Does not require multi-step reasoning loops  
- Does not involve multiple agents  
- Does not need graph-based execution flows  
- Follows a simple **Query → Retrieve → Generate** pipeline  

Using LangGraph would have added unnecessary architectural complexity.

---

## 🎯 Design Decision

The goal of this project was to:

- Demonstrate a clean RAG implementation  
- Keep the architecture simple and readable  
- Focus on retrieval accuracy and LLM integration  
- Make the system beginner-friendly and easy to extend  

Therefore, **LangChain was the most appropriate and efficient choice** for this use case.

---

## 📌 Future Improvements

- Add conversational memory  
- Support multiple video knowledge base  
- Include timestamp references in answers  
- Deploy as a web application  
- Add multilingual transcript support  

---

## 📜 License

This project is open-source and available under the MIT License.
