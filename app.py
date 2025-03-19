import streamlit as st
from utils.document_loader import load_documents
from utils.embedding import create_vector_store, query_vector_store
from utils.llm import query_gemini
from components.chat import display_chat_interface
from components.dashboard import display_dashboard
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set page configuration
st.set_page_config(page_title="Turbine Monitoring Assistant", layout="wide")

# Initialize session state variables
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None

# Main app layout
st.title("Turbine Monitoring Assistant")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    st.markdown("Upload your turbine documentation and data to the `documents` folder before running the app.")

    st.subheader("Model Settings")
    k_docs = st.slider("Number of reference documents", 1, 10, 3)

    if st.button("Load Documents"):
        with st.spinner("Loading documents..."):
            documents = load_documents()
            if documents:
                st.session_state.vector_store = create_vector_store(documents)
                st.success(f"Loaded {len(documents)} document chunks")
            else:
                st.error("No documents found or error loading documents")

# Display chat interface
display_chat_interface(k_docs)

# Display dashboard
display_dashboard()