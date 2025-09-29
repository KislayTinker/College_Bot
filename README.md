# 🤖 College AI Assistant

An intelligent, multilingual chatbot designed to provide instant answers to student queries, built for the Smart India Hackathon. This AI assistant helps bridge the communication gap in educational institutions.

-----

## 🌟 Introduction

In any busy college campus, administrative staff are often overwhelmed with repetitive student inquiries about deadlines, fees, and procedures. At the same time, students, especially those more comfortable in regional languages, face challenges getting clear and quick information.

Our **College AI Assistant** is a multilingual conversational bot that solves this problem. It ingests information from college circulars and FAQs to provide instant, accurate answers 24/7. By integrating with the college website and Telegram, it ensures that help is always just a message away, freeing up staff to handle more complex issues.

-----

## ✨ Key Features

  * **🧠 Intelligent NLP Core**: Moves beyond simple keyword matching using **Sentence Transformers** to understand the *meaning* behind a student's question, providing highly accurate answers.
  * **🌐 Multilingual Support**: Students can ask questions in their native language (supports 5+ regional languages). The bot translates the query, finds the answer, and translates it back.
  * **🗣️ Context-Aware Conversations**: Remembers the topic of conversation. If you ask about "admission fees" and then follow up with "what is the deadline?", it understands you're still talking about admissions.
  * **💬 Dual Platform Integration**: Seamlessly available on both the **college website** (as a pop-up widget) and on **Telegram** for on-the-go access.
  * **📝 Conversation Logging**: All interactions are logged for auditing and continuous improvement, helping administrators understand common student concerns.
  * **💪 Robust & Scalable**: Built with a clean Flask backend and a modern vanilla JS frontend, ensuring reliability and maintainability.

-----

## 🎥 Demo

Here's a quick look at the chatbot in action:

**Website Integration:**

*(Here, you should insert a GIF showing a user interacting with the chatbot on your college website. Record your screen while asking a few questions.)*
`![Website Demo GIF](link-to-your-website-demo.gif)`

**Telegram Integration:**

*(Insert another GIF showing a similar interaction on the Telegram mobile app.)*
`![Telegram Demo GIF](link-to-your-telegram-demo.gif)`

-----

## 🛠️ Tech Stack

This project is built with a modern and reliable technology stack:

  * **Backend**: Python, Flask
  * **NLP/ML**: `sentence-transformers`, `scikit-learn`
  * **Frontend**: HTML5, CSS3, Vanilla JavaScript
  * **Deployment**: Gunicorn, Nginx (or similar)
  * **Services**: Telegram Bot API

-----

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing.

### Prerequisites

  * Python 3.8+
  * pip (Python package installer)
  * A Telegram Bot Token from BotFather

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/college-chatbot.git
    cd college-chatbot
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    *(You will need to create a `requirements.txt` file by running `pip freeze > requirements.txt`)*

4.  **Set up environment variables:**

      * Create a file named `.env` in the project's root directory.
      * Add your Telegram Bot Token to this file:
        ```
        TELEGRAM_TOKEN="YOUR_TELEGRAM_TOKEN_HERE"
        ```

5.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    Your chatbot is now running locally\! The web interface is available at `http://127.0.0.1:5000`.

### Setting up the Telegram Webhook

To connect your running application to Telegram, you'll need to use a tool like **ngrok** to expose your local server to the internet.

1.  **Start ngrok** in a new terminal:

    ```bash
    ngrok http 5000
    ```

2.  **Copy the HTTPS URL** provided by ngrok (e.g., `https://random-string.ngrok.io`).

3.  **Set the webhook** by visiting the following URL in your browser. Replace `<YOUR_TOKEN>` and `<YOUR_NGROK_URL>` accordingly.

    ```
    https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=<YOUR_NGROK_URL>/webhook
    ```

You can now chat with your bot on Telegram\!

-----

## 📁 Project Structure

```
college-chatbot/
├── app.py              # Main Flask Application
├── frontend/           # All web interface files (HTML/CSS/JS)
├── services/           # Business logic (FAQ, NLP, Telegram)
├── routes/             # Flask blueprints (e.g., webhook)
├── utils/              # Helper utilities (e.g., logger)
├── data/               # CSV files and other data
├── logs/               # Conversation logs
├── .env                # Environment variables (Git-ignored)
└── README.md
```

-----
