import streamlit as st
from utils.embedding import query_vector_store
from utils.llm import query_gemini


def display_chat_interface(k_docs):
    """Display the chat interface"""
    st.subheader("Ask about your turbine operations")

    user_query = st.text_input("Enter your question:", key="user_input")

    if st.button("Submit") and user_query:
        with st.spinner("Generating response..."):
            # Retrieve relevant documents
            if st.session_state.vector_store:
                relevant_docs = query_vector_store(st.session_state.vector_store, user_query, k=k_docs)
                context = "\n\n".join([doc.page_content for doc in relevant_docs])

                # Show retrieved context in expander
                with st.expander("View retrieved context"):
                    st.markdown(context)
            else:
                st.warning("No documents loaded. Please load documents first.")
                context = "No context available."

            # Query Gemini
            response = query_gemini(user_query, context)

            # Add to chat history
            st.session_state.chat_history.append({"query": user_query, "response": response})

    # Display chat history
    if st.session_state.chat_history:
        st.subheader("Chat History")
        for i, chat in enumerate(st.session_state.chat_history):
            st.markdown(f"**User:** {chat['query']}")
            st.markdown(f"**Assistant:** {chat['response']}")
            st.divider()