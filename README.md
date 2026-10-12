🤖 AI Chatbot (Rule-Based & Regex Pattern Matching)

A responsive conversational AI chatbot built with Python and regular expressions (re) designed to understand user intents, handle common conversational workflows, and deliver structured, context-aware responses without external API latency.

🔗 Live Streamlit Demo: aichatbot-erul3czvrg3yj9ozedwtno.streamlit.app
💡 How the Project Works

    Input Normalization & Preprocessing:

        User inputs are normalized by stripping leading/trailing whitespace, converting text to lowercase, and handling basic punctuation to ensure uniform pattern evaluation.

    Regex Intent Matching & Pattern Extraction:

        The conversational engine utilizes compiled regular expressions (re.search and re.findall) with word boundaries (\b) to match user intents against predefined categories (e.g., greetings, inquiries, FAQs, technical support, and farewells).

        Extracts dynamic parameters and entities (such as names, dates, or keywords) from natural language inputs to personalize replies.

    Fallback & Graceful Error Handling:

        When user queries fall outside recognized rule patterns, the bot activates conversational fallback strategies to prompt clarifications without crashing or halting dialogue.

    Interactive Chat Interface:

        Implemented via Streamlit, providing real-time multi-turn conversational history management using st.session_state and conversational chat bubbles.

🛠️ Technology Stack

    Core Language: Python 3.x

    Pattern Matching & NLP Logic: Python standard library re (Regular Expressions)

    Web Interface: Streamlit (st.chat_message, st.chat_input, st.session_state)

🚀 How to Run the Project Locally
1. Clone the Repository
Bash

git clone <YOUR_REPOSITORY_URL>
cd AI_Chatbot

2. Set Up a Virtual Environment (Recommended)
Bash

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
Bash

pip install streamlit

4. Run the Streamlit Application
Bash

streamlit run app.py

The application will launch locally in your default web browser at http://localhost:8501.

🌐 Live Application

Access the hosted deployment directly in your browser:

👉 Open AI Chatbot
