import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🤖",
    layout="centered"
)

# App title
st.title("🤖 AI Study Buddy")

st.write(
    "Ask questions and learn with AI."
)

# Check API key
if not api_key:
    st.error(
        "OpenAI API key not found. "
        "Please add OPENAI_API_KEY to your .env file."
    )
    st.stop()

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Sidebar settings
st.sidebar.title("⚙️ Settings")

language = st.sidebar.selectbox(
    "🌐 Language",
    ["English", "Telugu", "Hindi"]
)

level = st.sidebar.selectbox(
    "🎓 Student Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# Main question box
question = st.text_area(
    "❓ What do you want to learn?",
    placeholder="Example: Explain Python loops in simple English."
)

# Ask AI button
if st.button("🚀 Ask AI"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    # Prompt for the AI
    prompt = f"""
You are an AI Study Buddy.

Student level: {level}
Preferred language: {language}

Explain the following question clearly:

{question}

Use simple examples where useful.
"""

    try:
        with st.spinner("🤖 AI is thinking..."):

            response = client.responses.create(
                model="gpt-5",
                input=prompt
            )

        st.subheader("🤖 AI Answer")

        st.write(response.output_text)

    except Exception as e:

        st.error(
            "Something went wrong while contacting the AI."
        )

        st.exception(e)