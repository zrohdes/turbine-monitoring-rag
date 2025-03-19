"""
Configuration settings for the Turbine Monitoring RAG application.
This file contains all the configurable parameters for the application.
"""

# Application settings
APP_TITLE = "Turbine Monitoring Assistant"
APP_DESCRIPTION = "A RAG-powered assistant for wind and gas turbine monitoring and optimization"
APP_ICON = "🔌"  # Icon displayed in the browser tab

# Model settings
DEFAULT_K_DOCS = 3  # Default number of documents to retrieve
GEMINI_MODEL = "gemini-pro"  # Gemini model to use
TEMPERATURE = 0.2  # Temperature for generation (lower is more deterministic)
MAX_TOKENS = 1024  # Maximum tokens for generation

# Document processing settings
CHUNK_SIZE = 1000  # Size of document chunks
CHUNK_OVERLAP = 100  # Overlap between chunks
EMBEDDING_MODEL = "text-embedding-ada-002"  # OpenAI embedding model

# Vector store settings
VECTOR_STORE_TYPE = "FAISS"  # Type of vector store to use
SIMILARITY_METRIC = "cosine"  # Similarity metric for vector search

# UI settings
THEME_COLOR = "#1E88E5"  # Primary theme color
SECONDARY_COLOR = "#FFC107"  # Secondary color for accents
BACKGROUND_COLOR = "#F5F7F9"  # Background color
TEXT_COLOR = "#333333"  # Text color

# Dashboard settings
REFRESH_INTERVAL = 300  # Dashboard refresh interval in seconds
CHART_HEIGHT = 400  # Height of charts in pixels
CHART_ANIMATION = True  # Whether to animate charts

# Debug settings
DEBUG_MODE = False  # Whether to run in debug mode
LOG_LEVEL = "INFO"  # Logging level