import streamlit as st
import google.generativeai as genai
# Title of the app
st.title("Google Gemini Q/A Bot")

# Input for user question
user_input = st.text_input("Ask your question:")

# Button to submit the question
if st.button("Get Answer"):
    if user_input:
        # Configure Gemini API
        genai.configure(api_key="aa")  # Replace with your actual API key

        # Initialize the Gemini model
        model = genai.GenerativeModel('gemini-pro')

        # Generate response
        response = model.generate_content(user_input)

        # Display the answer
        st.success(f"Answer: {response.text}")
    else:
        st.warning("Please enter a question.")