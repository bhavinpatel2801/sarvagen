import streamlit as st
import tempfile
import os
import re
from core.processor import route_input
from core.agent import agent_controller
from utils.display import show_response

def run_ui():
    st.set_page_config(page_title="SarvaGen", layout="centered")
    st.title("🎯 SarvaGen – Unified Gen AI System")
    st.markdown("Upload a **text**, **image**, **PDF**, or **audio** file to process.")

    uploaded_file = st.file_uploader("Upload File", type=["txt", "md", "jpg", "jpeg", "png", "pdf", "mp3", "wav", "m4a", "ogg"])
    user_text = st.text_area("Or enter your prompt here (optional):", height=150)

    if uploaded_file or user_text:
        if st.button("🔍 Process"):
            if uploaded_file:
                with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                st.success(f"📂 Uploaded file: {uploaded_file.name}")
                raw_result = route_input(tmp_path)
                agent_result = agent_controller(tmp_path, reasoning_text=user_text)

                if agent_result.endswith(".png"):
                    st.image(agent_result, caption="🖼️ Generated Image")
                elif agent_result.endswith(".wav"):
                    st.audio(agent_result)
                else:
                    show_response(raw_result, agent_result)
                os.unlink(tmp_path)

            elif user_text:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8') as tmp:
                    tmp.write(user_text)
                    tmp_path = tmp.name
                st.success("📝 Received text input")
                raw_result = route_input(tmp_path)
                agent_result = agent_controller(tmp_path)

                match = re.search(r"Result: (data/generated/[\w\-]+\.png)", agent_result)
                if match:
                    image_path = match.group(1)
                    st.image(image_path, caption="🖼️ Generated Image", use_column_width=True)
                elif agent_result.endswith(".wav"):
                    st.audio(agent_result)
                else:
                    show_response(raw_result, agent_result)
                os.unlink(tmp_path)


        