import streamlit as st 
import google.generativeai as genai

st.title("AI CHAT APPLICATION")

genai.configure(api_key="AIzaSyDuqMU6mN28Fchw-LXng896UxVKrL5KoVs")

text = st.text_input("Enter the question")

model = genai.GenerativeModel('gemini-pro') 
chat = model.start_chat(history=[])

if st.button("Click me"):

    response = chat.send_message(text) 
    st.write(response.text)