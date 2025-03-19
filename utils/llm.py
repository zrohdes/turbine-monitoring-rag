import streamlit as st
import google.generativeai as genai
from google.generativeai import GenerativeModel
import os


def query_gemini(query, context):
    """Query the Gemini LLM with the user's question and context"""
    try:
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            st.error("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")
            return "Error: Google API key not found"

        genai.configure(api_key=api_key)

        # Create the model
        model = GenerativeModel('gemini-pro')

        # Create the prompt with context
        prompt = f"""
        You are a specialized assistant for wind and gas turbine monitoring and optimization.
        Using the provided context, answer the user's question about turbine operations, 
        maintenance, or optimization. If you don't find the information in the context,
        use your general knowledge but make it clear that you're not using the specific
        context data.

        Context:
        {context}

        User Question: {query}

        Provide a detailed, technical answer that would be helpful for a turbine engineer or operator.
        Format your response using markdown for better readability.
        """

        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error querying Gemini: {e}")
        return f"Error: {str(e)}"