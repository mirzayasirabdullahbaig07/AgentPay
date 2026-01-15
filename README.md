# 💳🤖 AgentPay-AI

## Pay-Per-Use Generative AI Agent with Simulated USDC Billing

AgentPay-AI is a lightweight **pay-per-use GenAI agent platform** that simulates token-based billing (USDC-style) for AI tasks. It demonstrates how AI services can be monetized at the request level, similar to how real-world AI APIs charge users per token or request.

---

## 🚀 What Is AgentPay-AI?

AgentPay-AI is a **GenAI agent interface** built using Streamlit and Google Gemini models that:

- Accepts user tasks (prompts)
- Estimates token usage cost
- Deducts balance in simulated USDC
- Executes AI tasks only if sufficient balance exists

This project acts as a **proof-of-concept for AI monetization systems**.

---

## 🧠 Problem It Solves

Most AI demos ignore cost control and billing logic, which is unrealistic for production AI systems.

**AgentPay-AI addresses:**

- ❌ Unlimited AI usage without accountability  
- ❌ No cost transparency for GenAI usage  
- ❌ No simulation of real-world AI payment flows  

**It introduces:**

- ✅ Pay-per-use logic  
- ✅ Token-based cost estimation  
- ✅ Wallet-style balance control  
- ✅ Controlled access to AI agents  

---

## 🎯 Purpose of This Project

- Demonstrate **AI-as-a-Service (AIaaS)** billing logic  
- Simulate **USDC-style micro-payments** for AI agents  
- Build a foundation for:
  - AI SaaS products
  - Agent marketplaces
  - Crypto + AI integrations
- Serve as a **portfolio project** for GenAI / Web3 / SaaS roles

---

## ⚙️ Key Features

- 🔐 API key–based authentication  
- 💰 Simulated USDC wallet per session  
- 📊 Token-based cost estimation  
- 🧠 Google Gemini / PaLM text generation  
- 🎛️ Adjustable temperature & max tokens  
- 🖥️ Simple and intuitive Streamlit UI  

---

## 🧩 Tech Stack

### 🧠 AI & LLM
- Google Gemini / PaLM  
- `google-genai` Python SDK  

### 🖥️ Frontend
- Streamlit  

### 🔧 Backend / Logic
- Python 3.10+  
- Session-based state management  
- Token cost estimation logic  

### 🔐 Configuration
- `python-dotenv`  
- Environment variables for API keys  

---

## 🗂️ Project Structure

```text
agentpay-ai/
│
├── app.py              # Main Streamlit app
├── .env                # Environment variables (API keys)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
