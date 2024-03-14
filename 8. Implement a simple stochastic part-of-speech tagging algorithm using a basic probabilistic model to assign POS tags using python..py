import random
training_data = [
    ("I", "PRP"),
    ("love", "VBP"),
    ("eating", "VBG"),
    ("pizza", "NN"),
    ("with", "IN"),
    ("cheese", "NN"),
    ("and", "CC"),
    ("drinking", "VBG"),
    ("soda", "NN"),
]
def train_stochastic_pos_tagger(training_data):
    model = {}
    for word, pos_tag in training_data:
        if word in model:
            if pos_tag in model[word]:
                model[word][pos_tag] += 1
            else:
                model[word][pos_tag] = 1
        else:
            model[word] = {pos_tag: 1}
    for word in model:
        total_count = sum(model[word].values())
        for pos_tag in model[word]:
            model[word][pos_tag] /= total_count
    return model
def stochastic_pos_tag(text, model):
    tagged_text = []
    for word in text:
        if word in model:
            pos_tags = list(model[word].keys())
            probabilities = list(model[word].values())
            chosen_tag = random.choices(pos_tags, probabilities)[0]
            tagged_text.append((word, chosen_tag))
        else:
            tagged_text.append((word, "NN"))
    return tagged_text

# Example usage
text = ["I", "love", "eating", "pizza", "with", "cheese", "and", "drinking", "soda"]
model = train_stochastic_pos_tagger(training_data)
tagged_text = stochastic_pos_tag(text, model)
print("Stochastic POS Tagging:")
for word, pos_tag in tagged_text:
    print(f"{word}: {pos_tag}")
