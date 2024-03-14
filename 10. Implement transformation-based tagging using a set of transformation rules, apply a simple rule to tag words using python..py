import re
rules = [
    (r'\bI\b', 'PRP'),
    (r'\bam\b', 'VBP'),
    (r'\beating\b', 'VBG'),
    (r'\bpizza\b', 'NN'),
    (r'\bwith\b', 'IN'),
    (r'\bcheese\b', 'NN'),
    (r'\band\b', 'CC'),
    (r'\bdrinking\b', 'VBG'),
    (r'\bsoda\b', 'NN'),
]
def transform_based_tagging(text, rules):
    tagged_text = []
    for word in text.split():
        tagged = False
        for pattern, pos_tag in rules:
            if re.match(pattern, word):
                tagged_text.append((word, pos_tag))
                tagged = True
                break
        if not tagged:
            tagged_text.append((word, 'NN'))  
    return tagged_text
text = "I am eating pizza with cheese and drinking soda."
tagged_text = transform_based_tagging(text, rules)
for word, pos_tag in tagged_text:
    print(f"{word}: {pos_tag}")
