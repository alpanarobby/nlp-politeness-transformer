# -----------------------------
# 🔴 RUDE / IMPOLITE DETECTION
# -----------------------------

rude_words = [
    "shut up", "idiot", "stupid", "dumb", "hate you",
    "go away", "leave me alone", "you are useless",
    "nonsense", "what is wrong with you", "trash"
]

def is_rude(text):
    text = text.lower()
    for word in rude_words:
        if word in text:
            return True
    return False


# -----------------------------
# 🟢 ALREADY POLITE DETECTION
# -----------------------------

polite_keywords = [
    "please", "could you", "would you", "kindly",
    "thank you", "thanks", "appreciate", "sorry"
]

def is_already_polite(text):
    text = text.lower()
    for word in polite_keywords:
        if word in text:
            return True
    return False


# -----------------------------
# 🔵 POLITE TRANSFORMATION
# -----------------------------

polite_dict = {
    # Direct rude phrases
    "shut up": "could you please be quiet",
    "go away": "could you please leave",
    "leave me alone": "could you please give me some space",

    # Commands → polite requests
    "send me": "could you please send me",
    "give me": "could you please provide",
    "tell me": "could you please tell me",
    "show me": "could you please show me",
    "fix this": "could you please fix this",
    "do this": "could you please do this",

    # Time urgency softening
    "now": "at your convenience",
    "immediately": "as soon as possible",

    # Tone improvement
    "i want": "i would like",
    "i need": "i would appreciate",
    "why didn't you": "could you please explain why",
    "you should": "it would be helpful if you could",

    # Negative tone softening
    "this is bad": "this could be improved",
    "this is wrong": "this may not be correct",
    "this is terrible": "this is not ideal"
}


def make_polite(text):
    text_lower = text.lower()

    for k, v in polite_dict.items():
        text_lower = text_lower.replace(k, v)

    return text_lower