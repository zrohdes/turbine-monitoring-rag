import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os


@st.cache_resource
def create_vector_store(_documents):
    """Create a vector store from the processed documents"""
    try:
        # Initialize embeddings
        embeddings = OpenAIEmbeddings(
            model="text-embedding-ada-002",
            openai_api_key=os.environ.get("OPENAI_API_KEY")
        )

        # Create vector store
        vector_store = FAISS.from_documents(_documents, embeddings)

        return vector_store
    except Exception as e:
        st.error(f"Error creating vector store: {e}")
        return None


def query_vector_store(vector_store, query, k=3):
    """Query the vector store for similar documents"""
    if not vector_store:
        return []

    try:
        # Search for similar documents
        docs = vector_store.similarity_search(query, k=k)
        return docs
    except Exception as e:
        st.error(f"Error querying vector store: {e}")
        return []