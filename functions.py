import openai
import streamlit as st

def summarise(prompt):
    augmented_prompt = f"summarise this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=1,
            max_tokens=1000,
        )["choices"][0]["text"]
    except:
        st.write("There was an error =(")