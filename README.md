# 💬 Streamlit AI Chat App (Ollama + LangChain)

A simple AI-powered chat application built with Streamlit and Ollama (local LLMs).
It uses `st.session_state` to maintain conversation memory and provides a ChatGPT-like experience in the browser.

## 🚀 Features

- 🤖 Runs locally using Ollama (no API key required)
- 💬 Chat-style UI with Streamlit
- 🧠 Memory using session state
- ⚡ Fast and lightweight
- 🔁 Continuous conversation support

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🎈
- Ollama 🦙
- LangChain (for message handling)

## 📂 Project Structure

```
streamlit-chat-app/
│
├── main.py             # Streamlit frontend
├── model.py             # Ollama backend logic
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/shameershahzad/streamlit-chat-app.git
cd streamlit-chat-app
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac/Linux**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Ollama Model
Make sure [Ollama](https://ollama.com) is installed, then pull the model used by this app:

```bash
ollama pull llama3.2
```

### 5. Run Application
```bash
python -m streamlit run main.py
```

## 🧠 How It Works

Streamlit reruns the script on every interaction, so we use session state to store memory.

### Memory Storage
```python
st.session_state.memory = []
```

### Message Types

- HumanMessage → user input
- AIMessage → AI response

### Flow

1. User enters message
2. Message stored in session state
3. Sent to Ollama backend
4. AI generates response
5. Response stored in memory
6. UI reruns and displays full chat history

## ⚡ Key Concept

Streamlit is stateless, so:

👉 `st.session_state` acts as persistent memory for the chat

Without it, chat history resets on every rerun.
