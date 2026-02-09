# 💳🤖 AgentPay-AI

## Pay-Per-Use Generative AI Agent with Simulated USDC Billing

AgentPay-AI is a lightweight **pay-per-use GenAI agent platform** that simulates token-based billing (USDC-style) for AI tasks. It demonstrates how AI services can be monetized at the request level, similar to how real-world AI APIs charge users per token or request.

---

## Live Demo
[Click Here](https://agentpay07.streamlit.app/)


## Video Demo
https://github.com/user-attachments/assets/c6726ede-23b4-4a74-a111-819c3fe96efb

---

## 🚀 What Is AgentPay-AI?

AgentPay-AI is a **GenAI agent interface** built using Streamlit and Google Gemini models that:

- Accepts user tasks (prompts)
- Estimates token usage cost
- Deducts balance in simulated USDC
- Executes AI tasks only if sufficient balance exists

This project acts as a **proof-of-concept for AI monetization systems**.

---

## 📸 Screenshots
### 🏠 Home Page
<img width="1035" height="775" alt="image" src="https://github.com/user-attachments/assets/969854a6-0131-4bb1-b267-752ba275e041" />


### ✅ Functionality 1
<img width="922" height="693" alt="image" src="https://github.com/user-attachments/assets/efc59485-fa21-45ef-a6f7-93bdc3984ece" />


### ✅ Functionality 2
<img width="784" height="697" alt="image" src="https://github.com/user-attachments/assets/1224e129-279c-46f2-aad9-04e6092f710a" />


### ✅ Functionality 3
<img width="765" height="716" alt="image" src="https://github.com/user-attachments/assets/d9b4b6ba-2684-4c31-9a15-0403f57b3367" />

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
