# Ollama Streamlit Chat

A simple and interactive chat interface built with Streamlit for communicating with Ollama models.

## Overview

This application provides a web-based chat interface powered by Streamlit to interact with Ollama's language models. Users can have natural conversations with AI models hosted through Ollama.

## Prerequisites

- Python 3.6+
- Ollama installed and running locally
- Streamlit

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ajit421/ollama-streamlit-chat.git
cd ollama-streamlit-chat
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure Ollama is running on your system
2. Run the Streamlit application:
```bash
streamlit run app.py
```
3. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

4. if you want to run in network
```
streamlit run app.py --server.headless true
```
## Features

- Clean and intuitive chat interface
- Real-time responses from Ollama models
- Streamlit-powered web application

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Ollama](https://ollama.ai/) for the local LLM capabilities