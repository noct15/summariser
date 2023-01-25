import streamlit as st
import openai
import os
from functions import summarise

try:
    openai.api_key = os.getenv("OPENAI_KEY")
    
    # initialise state variable
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""
    
    st.title("Summariser")
    
    input_text = st.text_area(label="Enter full text:", value="", height=250)
    
    st.button(
        "Submit",
        on_click=summarise,
        kwargs={"prompt": input_text},
    )
    
    # configure text area to populate with current state of summary
    output_text = st.text_area(label="Summarised text:", value=st.session_state["summary"], height=250)
except:
    st.write("There was an error =(")