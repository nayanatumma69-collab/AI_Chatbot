import json
import random
import re
from datetime import datetime, timezone
from pathlib import Path

import nltk
import numpy as np
import pandas as pd
import streamlit as st
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="💬",
    layout="centered",
)

BASE_DIR = Path(__file__).resolve().parent
INTENTS_PATH = BASE_DIR / "intents.json"
TOKENIZER = RegexpTokenizer(r"[A-Za-z0-9]+")

def nltk_tokenize(text):
    """Tokenize text with NLTK without requiring downloaded corpus files."""
    return TOKENIZER.tokenize(text.lower())

@st.cache_resource
def load_intent_model():
    """Train the TF-IDF + Logistic Regression intent classifier from intents.json."""
    with INTENTS_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    patterns = []
    labels = []
    responses = {}
    for intent in data["intents"]:
        responses[intent["tag"]] = intent["responses"]
        for pattern in intent["patterns"]:
            patterns.append(pattern)
            labels.append(intent["tag"])

    vectorizer = TfidfVectorizer(
        tokenizer=nltk_tokenize,
        token_pattern=None,
        lowercase=False,
        ngram_range=(1, 2),
        sublinear_tf=True,
    )
    X = vectorizer.fit_transform(patterns)
    classifier = LogisticRegression(max_iter=1000, random_state=42)
    classifier.fit(X, labels)
    return vectorizer, classifier, responses, data["intents"]

vectorizer, classifier, responses_map, intents = load_intent_model()
CONFIDENCE_THRESHOLD = 0.18

def predict_intent(user_text):
    """Return the predicted intent and confidence, or None for unknown text."""
    cleaned = user_text.strip()
    if not cleaned:
        return None, 0.0

    features = vectorizer.transform([cleaned])
    if features.nnz == 0:
        return None, 0.0

    probabilities = classifier.predict_proba(features)[0]
    best_index = int(np.argmax(probabilities))
    confidence = float(probabilities[best_index])
    predicted_tag = classifier.classes_[best_index]

    if confidence < CONFIDENCE_THRESHOLD:
        return None, confidence
    return predicted_tag, confidence

FALLBACK_RESPONSES = [
    "I'm sorry, I didn't quite catch that. Could you please rephrase?",
    "I'm not sure I understand. You can ask about store hours, shipping, order tracking, or return policies.",
    "I don't have information on that yet. You can try asking about one of the supported customer-support topics.",
]

def create_response(user_text):
    """Generate a response and manage the basic order-ID follow-up flow."""
    text = user_text.strip()
    if not text:
        return "Please enter a message so I can help you.", None, 0.0

    # A real order-management system would verify an ID against a secure backend.
    # This demo intentionally does not claim to access real orders.
    if st.session_state.get("awaiting_order_id", False):
        st.session_state.awaiting_order_id = False
        response = (
            f"Thanks for sharing order ID '{text}'. "
            "Status: In Transit. Estimated delivery is within 2-3 business days."
        )
        return response, "order_id_submission", 1.0

    tag, confidence = predict_intent(text)
    if tag is None:
        return random.choice(FALLBACK_RESPONSES), None, confidence

    if tag == "track_order":
        st.session_state.awaiting_order_id = True
        return (
            "I can guide you through tracking your order. Please enter your Order ID. ",
            tag,
            confidence,
        )

    return random.choice(responses_map.get(tag, FALLBACK_RESPONSES)), tag, confidence

def log_exchange(user_text, bot_text, tag, confidence):
    st.session_state.logs.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user": user_text,
        "bot": bot_text,
        "intent": tag,
        "confidence": round(float(confidence), 4),
    })

st.title("💬 AI Customer Support Chatbot")
st.caption("NLTK tokenization · TF-IDF · Logistic Regression · Streamlit")
st.write(
    "Ask about store hours, order tracking, returns and refunds, payment methods, "
    "shipping, discounts, or human support."
)

with st.sidebar:
    st.header("About this project")
    st.write("A demo chatbot trained on example utterances from `intents.json`.")
    st.write("The intent model is trained when the app starts.")
    st.warning(
        "This is a demonstration. Store policies, contact details, and tracking "
        "responses are sample data."
    )
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.session_state.logs = []
        st.session_state.awaiting_order_id = False
        st.rerun()

    if st.session_state.get("logs"):
        log_json = json.dumps(st.session_state.logs, indent=2, ensure_ascii=False)
        st.download_button(
            "Download session history (JSON)",
            data=log_json,
            file_name="chatbot_session_history.json",
            mime="application/json",
        )

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI Support Assistant. How can I help you today?"}
    ]
if "logs" not in st.session_state:
    st.session_state.logs = []
if "awaiting_order_id" not in st.session_state:
    st.session_state.awaiting_order_id = False

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_text = st.chat_input("Type your customer-support question...")
if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    response, tag, confidence = create_response(user_text)
    st.session_state.messages.append({"role": "assistant", "content": response})
    log_exchange(user_text, response, tag, confidence)

    with st.chat_message("assistant"):
        st.markdown(response)
        if tag:
            st.caption(f"Detected intent: `{tag}` · confidence: {confidence:.2f}")
    st.rerun()

with st.expander("Supported intents"):
    intent_rows = []
    for intent in intents:
        intent_rows.append({
            "Intent": intent["tag"],
            "Example question": intent["patterns"][0] if intent["patterns"] else "",
        })
    st.dataframe(pd.DataFrame(intent_rows), use_container_width=True, hide_index=True)
