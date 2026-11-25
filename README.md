# FAQ Chatbot

A simple chatbot that answers questions using a list of FAQs. It uses NLTK to clean the text and cosine similarity to find the closest matching FAQ.

## How it works

1. **Collect FAQs:** questions and answers are stored in `faqs.json`.
2. **Preprocess:** each text is lowercased, tokenized, stripped of stopwords, and stemmed with NLTK.
3. **Match:** the questions are turned into TF-IDF vectors, and the user's question is compared to them with cosine similarity.
4. **Answer:** the best match is shown. If the score is below the threshold, the bot says it doesn't know.

## Files

| File | Purpose |
|---|---|
| `faqs.json` | The FAQ questions and answers |
| `preprocess.py` | Text cleaning with NLTK |
| `chatbot.py` | Matching logic and terminal chat |
| `chat_window.py` | Simple chat window (Tkinter) |

## Setup

```
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

## Run

Terminal chat:

```
python chatbot.py
```

Chat window:

```
python chat_window.py
```

## Example

```
You: when do I receive my salary
Bot: Salaries are paid on the last working day of every month.
```

## Customize

Edit `faqs.json` with your own questions and answers. Adding several wordings of the same question improves matching.