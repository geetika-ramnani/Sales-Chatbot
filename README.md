# 🛍️ FastAPI E-commerce Chatbot

This repository contains an **AI-powered customer support chatbot** built with **FastAPI**, **Groq's LLaMA model**, **MongoDB**, and a responsive **HTML/CSS/JavaScript frontend**.

Designed for integration with e-commerce platforms, the chatbot handles common customer queries like order tracking and refunds using both rule-based and AI-driven approaches.


## 🎯 Objective

The chatbot aims to **automate and streamline customer support** for an e-commerce platform by:

- ✅ Responding to **predefined queries** (e.g., _“How can I track my order?”_) with accurate, rule-based answers.
- 🧠 Using **Groq's `llama-3.3-70b-versatile` model** for flexible, dynamic responses to unrecognized queries.
- 💾 Storing **conversation history in MongoDB** for context-aware and personalized interactions.
- 🌐 Providing a **user-friendly web interface** for seamless customer interaction.

This project enhances the customer support experience while reducing the need for human agents, improving both response time and scalability.


## 🗂️ Project Structure

```
fastapi-chatbot/
├── app/
│   ├── __init__.py              # Package initializer
│   ├── main.py                  # FastAPI app entry point
│   ├── config.py                # Configuration (env variables, API keys)
│   ├── database.py              # MongoDB connection and logic
│   ├── chatbot.py               # Groq API integration and chatbot logic
│   └── models.py                # Pydantic models for requests and responses
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (excluded from version control)
├── README.md                    # Project documentation
└── Dockerfile                   # Docker configuration (optional)
```


## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- MongoDB (local or cloud instance)
- Groq API key
- Node.js (for frontend, if using)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-chatbot.git
cd fastapi-chatbot
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
MONGO_URI=your_mongodb_connection_string
```

4. Run the FastAPI application:

```bash
uvicorn app.main:app --reload
```


## 🧠 Model Integration

This project uses **Groq's `llama-3.3-70b-versatile`** via their API for AI-based dynamic responses. You can modify the logic in `app/chatbot.py` to tailor responses based on your use case.


## 📦 Deployment

You can deploy the app using Docker:

```bash
docker build -t fastapi-chatbot .
docker run -p 8000:8000 fastapi-chatbot
```


## 📄 License

MIT License. See [LICENSE](LICENSE) for details.


## ✨ Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.


## 📬 Contact

For support or questions, contact jimitchavdadev@gmail.com.