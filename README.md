# 🤖 AI Study Buddy

A beginner-friendly AI learning application built with Python, Streamlit, and the OpenAI API.

## 🚀 Features

* 🤖 Ask questions to AI
* 🌐 Select language
* 🎓 Select student level
* 💬 Interactive Streamlit interface
* 🔐 Secure API key management

## 🛠️ Technologies

* Python
* Streamlit
* OpenAI API
* python-dotenv
* Git
* GitHub

## 📁 Project Structure

```text
AI-Study-Buddy/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

## ⚙️ Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🔑 API Key

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Never share your real API key.

Make sure `.env` is included in `.gitignore`.

## ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## 🔄 Application Flow

```text
Student
   ↓
Streamlit Interface
   ↓
Enter Question
   ↓
Python
   ↓
OpenAI API
   ↓
AI Response
   ↓
Student
```

## 🎓 Learning Goals

This project demonstrates:

* Python application development
* Streamlit UI development
* AI API integration
* Environment variables
* API key security
* Git and GitHub

## 📌 Future Improvements

* PDF upload
* AI document summarization
* AI quizzes
* Personalized study plans
* Multi-language learning
* Student dashboard

## 📜 License

Educational project.
