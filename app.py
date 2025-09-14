import streamlit as st
import ollama

st.set_page_config(page_title="Chat", layout="centered")

st.title("Chat with Ollama Model")
st.write("Ask something below and get a streamed reply from the model.")
st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past messages
for role, content in st.session_state["messages"]:
    with st.chat_message(role):
        st.markdown(content)

# User input
if prompt := st.chat_input("Type your message"):
    st.session_state["messages"].append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Convert chat history into Ollama format
    ollama_messages = []
    for role, content in st.session_state["messages"]:
        role_name = "user" if role == "user" else "assistant"
        ollama_messages.append({"role": role_name, "content": content})

    # Stream model response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        stream = ollama.chat(
            model="gemma3:270m",
            messages=ollama_messages,  # ✅ send full history
            stream=True,
        )

        for chunk in stream:
            if chunk["message"]["content"]:
                full_response += chunk["message"]["content"]
                message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)
        st.session_state["messages"].append(("assistant", full_response))
