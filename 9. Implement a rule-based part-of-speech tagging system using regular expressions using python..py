import re

patterns = [
    (r'\b(?:I|you|he|she|it|we|they)\b', 'PRP'),
    (r'\b(?:am|is|are|was|were)\b', 'VBP'),
    (r'\b(?:have|has|had)\b', 'VB'),
    (r'\b(?:do|does|did)\b', 'VBP'),
    (r'\b(?:can|could|will|would|shall|should|may|might|must)\b', 'MD'),
    (r'\b(?:the|a|an)\b', 'DT'),
    (r'\b(?:on|in|at|by|for|with|to|from|through|over|under|above|below|between|among|into|out)\b', 'IN'),
    (r'\b(?:and|or|but)\b', 'CC'),
    (r'\b(?:noun|nouns|verb|verbs|adjective|adjectives|adverb|adverbs)\b', 'NN'),
    (r'\b(?:[A-Z][a-z]+)\b', 'NNP'),
    (r'\b(?:\d+\.?\d*)\b', 'CD'),
    (r'[^\s]+(?:ing)\b', 'VBG'),
    (r'\b(?:ing)\b', 'VBG'),
    (r'[^\s]+(?:ed)\b', 'VBD'),
    (r'\b(?:ed)\b', 'VBD'),
    (r'\b(?:ing)\b', 'VBG'),
]

def rule_based_pos_tagging(text, patterns):
    tagged_text = []
    for word in text.split():
        tagged = False
        for pattern, pos_tag in patterns:
            if re.match(pattern, word):
                tagged_text.append((word, pos_tag))
                tagged = True
                break
        if not tagged:
            tagged_text.append((word, 'NN'))
    return tagged_text

text = "I am eating pizza with cheese and drinking soda."
tagged_text = rule_based_pos_tagging(text, patterns)
for word, pos_tag in tagged_text:
    print(f"{word}: {pos_tag}")
