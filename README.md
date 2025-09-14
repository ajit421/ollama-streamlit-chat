# Ollama Streamlit Chat

A chat UI built with Streamlit to interact with local Ollama language models (e.g. `gpt-oss`, `gemma3`, `mistral`, `deepseek` ).  
Keeps conversation history, streams responses in real time, and has a clean interface.

---

## 🧰 Features

- Interactive chat interface: user and assistant messages displayed in sequence  
- Streaming responses from the model (partial replies appear as they are generated)  
- Conversation memory: the model sees the full history of your previous exchanges in the current session  
- Customizable UI (you can adjust CSS for background, message alignment, etc.)

---

## 🚀 Prerequisites

Make sure you have:

- Python 3.7 or higher  
- [Ollama](https://ollama.com/) installed and running on your machine  
- Basic terminal/command line usage skills  

---

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ajit421/ollama-streamlit-chat.git
   cd ollama-streamlit-chat
   ```

2. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Setup & Running

1. Make sure Ollama is running and that the model you want to use is available, e.g.:

   ```bash
   ollama pull gemma3:270m
   ollama serve
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open your browser and go to the URL shown by Streamlit (usually `http://localhost:8501`).

4. (Optional) If you want to run it headless / on a server without opening a browser:

   ```bash
   streamlit run app.py --server.headless true
   ```

---


## 📁 File Structure

```
ollama-streamlit-chat/
│
├── app.py             # Main Streamlit app
├── requirements.txt   # Dependencies
├── README.md          # Project documentation (this file)
└── .gitignore         # Ignores venv, cache, etc.
```

---


## 🧠 How It Works

* The app keeps a list of message tuples (`role`, `text`) in `st.session_state["messages"]`.
* Every time you send a prompt, the app sends **all** past messages to the Ollama API via the Python client, so the model has context.
* While the model generates its reply, the UI shows partial results (streaming) for better interactivity.

---

## 🎨 UI Customization Tips

You can tweak:

* Background color (via CSS injection in `app.py`)
* Alignment of user vs assistant messages (right / left)
* Style of message “bubbles” (padding, colors, borders)

If you want white background, for example:

```python
st.markdown(
    """
    <style>
        .stApp {
            background-color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
```

---

## 🛠️ Troubleshooting

| Problem                                                 | Likely Cause                                                    | What To Do                                           |
| ------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------- |
| No response when you send a message                     | Ollama server not running or model not pulled                   | Run `ollama serve` and `ollama pull <model>`         |
| Messages keep getting cut off or streaming doesn’t work | Wrong version of Ollama or Python client; `stream=True` missing | Update packages, make sure `stream=True` in the call |
| UI doesn’t look right (colors, alignment)               | CSS class names may have changed; your custom CSS isn’t loaded  | Inspect with browser dev tools; adjust CSS selectors |

