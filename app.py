import streamlit as st
import string
import json

st.set_page_config(
    page_title="AI Chatbot",page_icon="🤖"
)

st.title("🤖 My AI Chatbot")
st.write("Hello! Welcome to my AI chatbot.")

with open("intents.json","r",encoding="utf-8") as file:
    data=json.load(file)

intents=data["intents"]

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_message = st.chat_input("Type your message here...")


if user_message:
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.write(user_message)

    user_text = user_message.lower().strip().translate(
    str.maketrans("", "", string.punctuation)
)

    tokens = user_text.split()
    

    answer = None

    for intent in intents:
        if intent["tag"] == "fallback":
            continue

        for pattern in intent["patterns"]:
            pattern_text = pattern.lower().strip().translate(
                str.maketrans("", "", string.punctuation)
            )

            if user_text == pattern_text:
                answer = intent["responses"][0]
                break

        if answer is not None:
            break

    if answer is None:
        for intent in intents:
            if intent["tag"] == "fallback":
                continue

            for pattern in intent["patterns"]:
                pattern_text = pattern.lower().strip().translate(
                    str.maketrans("", "", string.punctuation)
                )

                if " " in pattern_text and (
                    f" {pattern_text} " in f" {user_text} "
                ):
                    answer = intent["responses"][0]
                    break

            if answer is not None:
                break

    if answer is None:
        for intent in intents:
            if intent["tag"] == "fallback":
                continue

            for pattern in intent["patterns"]:
                pattern_text = pattern.lower().strip().translate(
                    str.maketrans("", "", string.punctuation)
                )

                if " " not in pattern_text and pattern_text in tokens:
                    answer = intent["responses"][0]
                    break

            if answer is not None:
                break

    if answer is None:
        fallback = next(
            (
                intent for intent in intents
                if intent["tag"] == "fallback"
            ),
            None
        )

        if fallback:
            answer = fallback["responses"][0]
        else:
            answer = (
                "Sorry, I don't know that yet. Please ask me about "
                "AI, Machine Learning, Python, or Data Science."
            )


    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)