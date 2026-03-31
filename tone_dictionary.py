# 🔴 RUDE WORDS
rude_words = [
    "shut up", "idiot", "stupid", "dumb", "hate you",
    "go away", "leave me alone", "you are useless"
]

def is_rude(text):
    text = text.lower()
    return any(word in text for word in rude_words)


# 🟢 POLITE DETECTION
polite_keywords = [
    "please", "could you", "would you", "kindly",
    "thank you", "thanks", "appreciate", "sorry",
    "may i", "can you", "would it be possible"
]

def is_already_polite(text):
    text = text.lower()
    return any(word in text for word in polite_keywords)


# 🔵 TRANSFORMATION
polite_dict = {
    "shut up": "could you please be quiet",
    "send me": "could you please send me",
    "give me": "could you please provide",
    "tell me": "could you please tell me",
    "do this": "could you please do this",
    "fix this": "could you please fix this",
    "now": "at your convenience",
    "immediately": "as soon as possible",
    "i want": "i would like",
    "i need": "i would appreciate",
    "you should": "it would be helpful if you could"
}

def make_polite(text):
    text_lower = text.lower()
    for k, v in polite_dict.items():
        text_lower = text_lower.replace(k, v)
    return text_lower.capitalize()