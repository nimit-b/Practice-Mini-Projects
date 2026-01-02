# ============================================================
# MAXIMAL LOCAL AI SYSTEM (CPU-ONLY, SINGLE FILE)
# Demonstrates SUPERVISED, UNSUPERVISED, REINFORCEMENT LEARNING
# ============================================================

import os
import json
import pickle
import random
import warnings
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# ------------------ SAFETY / CLEAN OUTPUT ------------------
warnings.filterwarnings("ignore", module="wikipedia")

# ------------------ FORCE CPU ------------------
torch.device("cpu")
torch.set_num_threads(2)

# ------------------ FILES ------------------
DATA_DIR = "ai_data"
INTENT_FILE = f"{DATA_DIR}/intent_data.json"
TOPIC_FILE = f"{DATA_DIR}/topic_data.json"
MODEL_FILE = f"{DATA_DIR}/intent_model.pt"
QTABLE_FILE = f"{DATA_DIR}/qtable.pkl"

os.makedirs(DATA_DIR, exist_ok=True)

# ============================================================
# RULE-BASED CONTROL (CRITICAL)
# ============================================================

def is_greeting(text):
    text = text.lower().strip()
    return text in {
        "hi", "hello", "hey", "yo",
        "good morning", "good afternoon", "good evening"
    }

def is_exit(text):
    return text.lower().strip() in {"exit", "quit", "bye"}

# ============================================================
# DATA LOADERS
# ============================================================

def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

intent_data = load_json(INTENT_FILE, {
    "texts": ["what is physics", "who are you", "tell me about science"],
    "labels": ["question", "question", "statement"]
})

topic_data = load_json(TOPIC_FILE, {
    "texts": ["physics studies matter", "football is a sport", "python is programming"],
    "labels": ["science", "sports", "technology"]
})

# ============================================================
# SUPERVISED LEARNING (INTENT CLASSIFIER)
# ============================================================

class IntentNet(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, num_classes)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

intent_vectorizer = TfidfVectorizer(max_features=300)
X_intent = intent_vectorizer.fit_transform(intent_data["texts"]).toarray()

intent_labels = sorted(set(intent_data["labels"]))
intent_to_idx = {l:i for i,l in enumerate(intent_labels)}
y_intent = np.array([intent_to_idx[l] for l in intent_data["labels"]])

intent_model = IntentNet(X_intent.shape[1], len(intent_labels))
optimizer = optim.Adam(intent_model.parameters(), lr=0.01)
loss_fn = nn.CrossEntropyLoss()

def train_intent():
    X = torch.tensor(X_intent, dtype=torch.float32)
    y = torch.tensor(y_intent, dtype=torch.long)
    for _ in range(50):
        optimizer.zero_grad()
        loss = loss_fn(intent_model(X), y)
        loss.backward()
        optimizer.step()

train_intent()

# ============================================================
# UNSUPERVISED LEARNING (TOPIC CLUSTERING)
# ============================================================

topic_vectorizer = TfidfVectorizer(max_features=300)
X_topic = topic_vectorizer.fit_transform(topic_data["texts"]).toarray()

if len(topic_data["texts"]) >= 3:
    kmeans = KMeans(n_clusters=min(3, len(topic_data["texts"])), n_init=10)
    kmeans.fit(X_topic)
else:
    kmeans = None

# ============================================================
# REINFORCEMENT LEARNING (Q-LEARNING)
# ============================================================

ACTIONS = ["answer", "classify", "ask_clarify"]

if os.path.exists(QTABLE_FILE):
    with open(QTABLE_FILE, "rb") as f:
        Q = pickle.load(f)
else:
    Q = {}

def choose_action(state):
    if state not in Q:
        Q[state] = {a: 0.0 for a in ACTIONS}
    return max(Q[state], key=Q[state].get)

def update_q(state, action, reward):
    Q[state][action] += 0.1 * (reward - Q[state][action])
    with open(QTABLE_FILE, "wb") as f:
        pickle.dump(Q, f)

# ============================================================
# PREDICTION HELPERS
# ============================================================

def predict_intent(text):
    vec = intent_vectorizer.transform([text]).toarray()
    x = torch.tensor(vec, dtype=torch.float32)
    with torch.no_grad():
        out = intent_model(x)
        idx = out.argmax().item()
    return intent_labels[idx]

def predict_topic(text):
    vec = topic_vectorizer.transform([text]).toarray()
    if kmeans:
        idx = kmeans.predict(vec)[0]
        return topic_data["labels"][idx]
    return "unknown"

# ============================================================
# MAIN LOOP
# ============================================================

def main():
    print("\n[BOOT] MAXIMAL LOCAL AI SYSTEM (FINAL)")
    print("CPU-only | Real Learning | Honest Behavior")
    print("Type 'exit' to quit.\n")

    while True:
        user = input("You: ").strip()
        if not user:
            continue

        if is_exit(user):
            print("AI: Goodbye.")
            break

        # -------- RULE-BASED GREETING (HARD GATE) --------
        if is_greeting(user):
            print("AI: Hello. I am a local learning AI.")
            continue

        # -------- INTENT (SUPERVISED) --------
        intent = predict_intent(user)

        # -------- STATE (FOR RL) --------
        state = f"{intent}|{len(user.split())}"
        action = choose_action(state)

        # -------- ACTION EXECUTION --------
        if action == "answer":
            topic = predict_topic(user)
            print(f"AI: This seems related to '{topic}'.")
        elif action == "classify":
            print(f"AI: Your input intent looks like '{intent}'.")
        else:
            print("AI: Can you clarify what you want?")

        # -------- FEEDBACK --------
        fb = input("Was this correct? (y/n): ").lower()
        if fb == "y":
            update_q(state, action, +1)
        else:
            update_q(state, action, -1)
            correct_intent = input("Correct intent (question/statement): ").strip()
            intent_data["texts"].append(user)
            intent_data["labels"].append(correct_intent)
            save_json(INTENT_FILE, intent_data)
            print("AI: Learned from correction.")

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()
