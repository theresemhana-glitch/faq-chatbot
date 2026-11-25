import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess

THRESHOLD = 0.2

with open("faqs.json") as f:
    faqs = json.load(f)

questions = [item["question"] for item in faqs]
cleaned = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(cleaned)


def find_best_match(user_text):
    user_clean = preprocess(user_text)
    user_vector = vectorizer.transform([user_clean])
    scores = cosine_similarity(user_vector, matrix)[0]
    best = scores.argmax()
    return faqs[best], scores[best]


def get_answer(user_text):
    faq, score = find_best_match(user_text)
    if score < THRESHOLD:
        return "Sorry, I don't know the answer to that."
    return faq["answer"]


if __name__ == "__main__":
    print("FAQ bot ready. Type 'quit' to exit.")
    while True:
        user_text = input("You: ")
        if user_text.lower() == "quit":
            break
        print("Bot:", get_answer(user_text))