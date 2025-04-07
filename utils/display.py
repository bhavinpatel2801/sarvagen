# utils/display.py

import streamlit as st

def show_response(input_text: str, agent_trace: str):
    st.markdown("## 🔤 Original Input")
    st.code(input_text)

    st.markdown("## 🧠 Agent Reasoning + Tool Use")
    st.markdown(agent_trace)

def show_multimodal_response(input_text: str, agent_trace: str, output_block):
    show_response(input_text, agent_trace)

    st.markdown("## 📤 Final Output")
    st.write(output_block)
