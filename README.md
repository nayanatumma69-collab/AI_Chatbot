# 🤖 AI Customer Support Chatbot

## 🚀 Live Demo

**Try the application here:** [AI Customer Support Chatbot](https://aichatbot-erul3czvrg3yj9ozedwtno.streamlit.app/)

## 📌 Project Overview

The AI Customer Support Chatbot is a Python-based application designed to answer common customer queries automatically. It identifies the intent behind a user's message and provides an appropriate response based on predefined intents and responses.

The chatbot demonstrates how Natural Language Processing (NLP) and Machine Learning can be used to build a simple customer support automation system.

## ⚙️ How the Project Works

1. **User Input:** The user enters a question or message through the Streamlit chat interface.
2. **Text Preprocessing:** NLTK's RegexpTokenizer helps tokenize the user's input into individual words.
3. **Text Vectorization:** TF-IDF converts the text into numerical features that the machine learning model can process.
4. **Intent Classification:** A Logistic Regression classifier predicts the intent of the user's message.
5. **Response Generation:** The chatbot selects a response associated with the predicted intent from the intents dataset.
6. **Fallback Handling:** If the chatbot cannot confidently identify the intent, it provides a fallback response.
7. **Conversation Interaction:** The Streamlit interface supports chat interaction and includes a simple follow-up flow for order-related queries.

## 🛠️ Technologies Used

- **Python** – Core programming language
- **Streamlit** – Web interface and interactive chatbot
- **NLTK** – Text tokenization and NLP preprocessing
- **Scikit-learn** – TF-IDF vectorization and Logistic Regression classification
- **NumPy** – Numerical operations
- **Pandas** – Data handling and organization
- **JSON** – Storage of intents, patterns, and responses

## ✨ Key Features

- Interactive customer support chat interface
- Machine learning-based intent classification
- TF-IDF text feature extraction
- Predefined responses for common customer queries
- Fallback response for unrecognized queries
- Basic order-related follow-up interaction
- Conversation history available during the session
- Option to download the conversation log as a JSON file
- Streamlit-based web deployment

## 💻 How to Run the Project Locally

### Prerequisites

- Python 3.9 or later
- pip package manager
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

Replace `YOUR_GITHUB_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ai-customer-support-chatbot.git
```

Navigate to the project directory:

```bash
cd ai-customer-support-chatbot
```

Alternatively, download the repository as a ZIP file and extract it.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit Application

```bash
streamlit run app.py
```

### Step 4: Open the Application

Streamlit will display a local URL in your terminal, usually:

```text
http://localhost:8501
```

Open this URL in your browser to interact with the chatbot.

## 📂 Project Structure

```text
ai-customer-support-chatbot/
│
├── app.py
├── intents.json
├── requirements.txt
├── README.md
├── .gitignore
└── notebooks/
    └── AI_Chatbot.ipynb
```

- `app.py` – Main Streamlit application and chatbot logic
- `intents.json` – Predefined intents, example patterns, and responses
- `requirements.txt` – Python dependencies
- `README.md` – Project documentation
- `notebooks/` – Original development notebook, if included

## ⚠️ Limitations

- The chatbot uses predefined intents and responses, so it may not understand every question.
- Order-related responses are demonstrations; the application does not connect to a live order management database.
- Response quality depends on the patterns, training data, and intent classification.

## 🔮 Future Improvements

- Integrate a live order management system or customer database.
- Add more intents and training examples.
- Implement contextual conversation memory.
- Explore transformer-based NLP models or Large Language Models (LLMs).
- Add multilingual support and analytics.

## 🎯 Learning Outcomes

This project demonstrates practical skills in Python, NLP preprocessing, text vectorization, supervised machine learning, intent classification, and Streamlit application development.

## 👩‍💻 Author

Developed as an AI learning and portfolio project to demonstrate a machine learning-based customer support chatbot.
