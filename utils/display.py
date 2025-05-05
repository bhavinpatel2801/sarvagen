# Import Streamlit library for creating interactive web apps
import streamlit as st

# === Display text input and agent's toolchain trace ==
def show_response(input_text: str, agent_trace: str):
    st.markdown("## 🔤 Original Input")               # Display the original user input as a code block
    st.code(input_text)

    st.markdown("## 🧠 Agent Reasoning + Tool Use")   # Display the agent's internal reasoning and tool usage
    st.markdown(agent_trace)

# === Extended version to also show the final output (e.g., image, text, audio) ===
def show_multimodal_response(input_text: str, agent_trace: str, output_block):

    # Reuse the same layout to show input and agent trace
    show_response(input_text, agent_trace)

    # Add a new section to display the tool's output result (could be any type: text, image, etc.)
    st.markdown("## 📤 Final Output")
    st.write(output_block)    # Streamlit auto-renders appropriate format (image, text, audio, etc.)
