# Andriod--kuttapan
AI Customer Support Chatbot with Sentiment Analysis

An intelligent AI-powered Customer Support Chatbot that detects customer sentiment (Positive, Negative, and Neutral) and responds with empathetic, context-aware replies. This project enhances a traditional chatbot by integrating Natural Language Processing (NLP) for emotion detection and intent recognition.

📌 Project Overview

This project extends a customer support chatbot by adding Sentiment Analysis. The chatbot analyzes the user's message, identifies the customer's emotional state, detects the user's intent, and generates an appropriate response.

The chatbot is designed to improve customer satisfaction by responding differently based on the user's emotions.

🚀 Features
😊 Sentiment Analysis (Positive, Neutral, Negative)
🎯 Intent Detection
💬 Emotion-aware Responses
📊 Sentiment Confidence Score
📝 Chat History Logging
🕒 Conversation Timestamp
🤖 Interactive Command-Line Chatbot
📁 Automatic Chat History Saving
🛠 Technologies Used
Python 3.x
NLTK
VADER Sentiment Analyzer
Datetime
File Handling
📂 Project Structure
AI-Customer-Support-Chatbot/
│
├── chatbot.py
├── chat_history.txt
├── requirements.txt
├── README.md
└── screenshots/
    ├── chatbot_output.png
    └── sentiment_result.png
⚙ Installation

Clone the repository:

git clone https://github.com/your-username/AI-Customer-Support-Chatbot.git

Go to the project folder:

cd AI-Customer-Support-Chatbot

Install dependencies:

pip install nltk

Download the VADER lexicon:

import nltk
nltk.download('vader_lexicon')

Run the chatbot:

python chatbot.py
🧠 How It Works
User enters a message.
The chatbot analyzes the sentiment using VADER Sentiment Analyzer.
The chatbot identifies the user's intent (Greeting, Order, Refund, Complaint, Thanks, Goodbye, etc.).
Based on both sentiment and intent, it generates an empathetic response.
The conversation is displayed and saved to chat_history.txt.
🔄 Workflow
User Message
      │
      ▼
Sentiment Analysis
      │
      ▼
Intent Detection
      │
      ▼
Response Generation
      │
      ▼
Display Response
      │
      ▼
Save Chat History
💬 Example Conversation
You: My order is delayed and I'm really angry.

Detected Intent:
Complaint

Detected Sentiment:
Negative

Confidence Score:
-0.82

Bot:
I'm really sorry for the inconvenience you've experienced.
Please provide your Order ID so I can assist you immediately.
You: Thank you for your help!

Detected Intent:
Thanks

Detected Sentiment:
Positive

Confidence Score:
0.91

Bot:
You're most welcome!
We're always here to help.
📈 Expected Outcome

The chatbot is able to:

Detect customer emotions accurately.
Respond politely and empathetically.
Improve customer interaction quality.
Reduce frustration during support conversations.
Simulate a real customer support assistant.
📊 Evaluation Criteria
Criteria	Description
Sentiment Detection Accuracy	Correctly identifies Positive, Neutral, and Negative emotions
Response Quality	Generates suitable responses according to user sentiment
Intent Recognition	Correctly identifies customer requests
Customer Satisfaction	Provides empathetic and context-aware conversations
Chat Logging	Stores conversation history for future analysis
📷 Sample Output
=======================================================
AI CUSTOMER SUPPORT CHATBOT
=======================================================

You: Hello

Intent      : greeting
Sentiment   : Neutral
Confidence  : 0.0

Bot:
Hello! Welcome to Customer Support.
How can I assist you today?

-------------------------------------------------------

You: My delivery is very late and I'm disappointed.

Intent      : complaint
Sentiment   : Negative
Confidence  : -0.71

Bot:
I'm sorry for the inconvenience.
Please provide your Order ID so I can help resolve this issue.
🔮 Future Enhancements
Streamlit Web Interface
Flask REST API
Voice Input and Speech Recognition
Text-to-Speech Responses
Hugging Face Transformer-based Sentiment Analysis (BERT)
SQLite/MySQL Database Integration
Customer Satisfaction Analytics Dashboard
Human Agent Escalation
Multi-language Support
AI-powered Responses using OpenAI or Gemini APIs
📚 Learning Outcomes

This project demonstrates practical implementation of:

Natural Language Processing (NLP)
Sentiment Analysis
Intent Detection
Rule-based Chatbot Development
Customer Support Automation
Python Programming
File Handling
Data Logging
👨‍💻 Author

Rooben Varghese Rajan

📄 License

This project is developed for educational and internship purposes. Feel free to modify and extend it for learning and research.
