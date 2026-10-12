# AI Customer Support Chatbot

A Streamlit web chatbot based on the intent dataset from the original `AI_Chatbot.ipynb` notebook.

## Features
- 10 predefined customer-support intents loaded from `intents.json`
- NLTK tokenization
- TF-IDF features and Logistic Regression intent classification
- Confidence threshold and fallback responses
- Basic multi-turn order-ID prompt
- Session conversation history with JSON download
- Streamlit chat interface

## Important demo limitation
The order-tracking flow does **not** connect to a real order database. Store hours, policies, discounts, and support contact details are sample responses and should be replaced with verified business information before real use.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy for free
1. Create a GitHub repository named `ai-customer-support-chatbot`.
2. Upload `app.py`, `intents.json`, `requirements.txt`, `README.md`, and `.gitignore` to the repository root.
3. Open https://share.streamlit.io and sign in with GitHub.
4. Choose **Create app**, select the repository and `main` branch, and set the app file path to `app.py`.
5. Click **Deploy**.

The original notebook is preserved in `notebooks/` for reference. Streamlit Community Cloud runs `app.py`, not the notebook.

## Project structure
- `app.py` — Streamlit UI and classifier
- `intents.json` — training utterances and responses
- `requirements.txt` — Python dependencies
- `notebooks/AI_Chatbot.ipynb` — original Colab notebook
