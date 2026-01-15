import os
import streamlit as st
from google.genai import Client
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("Please set your GOOGLE_API_KEY in .env")
    st.stop()

client = Client(api_key=API_KEY)

if "balance" not in st.session_state:
    st.session_state.balance = 1.0

def estimate_cost(text):
    tokens = len(text) / 4
    return round(tokens * 0.00001, 4)

def run_gemini(prompt, model_name="text-bison-001"):
    try:
        # This is the correct call in the latest google-genai
        response = client.text.generate(
            model=model_name,
            prompt=prompt,
            max_output_tokens=300,
            temperature=0.7
        )
        return response.output_text
    except Exception as e:
        return f"Error generating text: {e}"

# Streamlit UI
st.title("AgentPay-AI 💳🤖")
st.subheader("Pay-Per-Use GenAI Agent (Simulated USDC)")

st.write("💰 Balance:", st.session_state.balance, "USDC")

model_choice = st.selectbox("Select Model", ["text-bison-001", "gemini-1", "gemini-1.5-t"])
temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
max_tokens = st.slider("Max Tokens", 50, 1000, 300, 50)
task = st.text_area("Enter your task")

if st.button("Run Agent"):
    if not task.strip():
        st.warning("Please enter a task")
    else:
        cost = estimate_cost(task)
        if st.session_state.balance < cost:
            st.error("Insufficient USDC balance")
        else:
            st.session_state.balance -= cost
            result = run_gemini(task, model_name=model_choice)
            st.success(f"Cost: {cost} USDC")
            # st.write("### Result")
            # st.write(result)
