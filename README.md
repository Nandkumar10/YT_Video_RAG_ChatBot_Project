🎬 YouTube Video RAG ChatBot Project

An AI-driven chatbot that allows users to ask questions about any YouTube video and receive accurate answers based on the video’s content using Retrieval-Augmented Generation (RAG) with LangChain and vector embeddings.

🧠 About

This project lets you extract transcripts from YouTube videos, transform them into embeddings in a vector database, and build an intelligent chatbot that can:

✔ Understand video content
✔ Answer user questions with context-aware responses
✔ Provide summaries, explanations, and detailed info from videos

Instead of just feeding the video into an LLM, this system uses RAG to retrieve relevant chunks of the transcript before generating answers, improving accuracy and relevance.

🚀 Features

✔ Fetch YouTube video transcripts
✔ Convert transcript text into embeddings
✔ Store embeddings for fast retrieval
✔ Perform semantic search over video content
✔ Answer user questions with detailed responses
✔ Built using LangChain and vector database

🧱 Tech Stack

Python

LangChain

HuggingFace / LLM API

Vector Database (FAISS/Chroma)

YouTube Transcript Fetch

Streamlit UI (for interactive chat)


🛠 How It Works

User enters a YouTube video link

Video transcript is fetched automatically

Transcript is split into smaller chunks

Each chunk is embedded into a vector store

User asks a question in the UI

Relevant chunks are retrieved using vector similarity

The LLM generates a context-aware answer

🧪 Example Use Cases

“What are the key points explained in the video?”

“Summarize the speaker’s recommendations.”

“What tool did the presenter mention at minute 8:45?”

“Explain the concept of X from the video.”


🤔 Why LangChain Instead of LangGraph?

In this project, LangChain was used instead of LangGraph because the application follows a straightforward RAG pipeline and does not require complex agent workflows.

✅ Why LangChain Was Chosen

This project involves:

Loading YouTube transcripts

Splitting text into chunks

Creating embeddings

Storing them in a vector database

Retrieving relevant context

Generating responses using an LLM

This is a linear and well-defined workflow, which LangChain handles efficiently using:

Document Loaders

Text Splitters

Embedding Models

Vector Stores

Retrievers

LLM Chains

LangChain provides all the required abstractions for building a clean and modular RAG system without additional orchestration complexity.

🧠 Why LangGraph Was Not Used

LangGraph is more suitable for:

Multi-agent systems

Complex branching logic

Stateful workflows

Tool-calling agents with decision loops

Advanced conversational memory management

Since this project:

Does not require multi-step decision-making

Does not involve multiple agents

Does not need graph-based execution flows

Follows a simple query → retrieve → generate pipeline

Using LangGraph would have added unnecessary architectural complexity.

🎯 Design Decision

The goal of this project was to:

Demonstrate a clean RAG implementation

Keep the architecture simple and readable

Focus on retrieval accuracy and LLM integration

Make the system beginner-friendly and easy to extend

Therefore, LangChain was the most appropriate and efficient choice for this use case.
