# Course Query Chatbot

This project is a Course Query Chatbot built using LangChain and Flask. The chatbot extracts data from a website, creates embeddings using LangChain, stores them in a FAISS vector store, and provides a Flask RESTful API to query the vector store.

## Introduction

The Course Query Chatbot is designed to help users find information about various courses listed on the Brainlox website. It uses LangChain for creating embeddings and FAISS for efficient similarity search. The chatbot provides a simple RESTful API to query the course data and retrieve the most relevant course details.

## Features

- **Data Extraction**: Scrapes course data from the Brainlox website.
- **Embeddings Creation**: Uses LangChain's HuggingFaceEmbeddings to create embeddings for the course descriptions.
- **Vector Store**: Stores the embeddings in a FAISS vector store for efficient similarity search.
- **Flask RESTful API**: Provides a RESTful API to query the vector store and retrieve relevant course details.

## Task Requirements

1. **Extract data from** [Brainlox Technical Courses](https://brainlox.com/courses/category/technical) **using URL loaders from LangChain**
2. **Create embeddings and store them in a vector store**
3. **Create a Flask RESTful API to handle the conversation**

## Installation

To install and run the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone <your-github-repo-url>
   cd <repository-name>
