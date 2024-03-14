import re
text = "The quick brown fox jumps over the lazy dog."
pattern = r'\b(?:fox|dog)\b'
matches = re.findall(pattern, text)
print("Matches found:", matches)
replaced_text = re.sub(pattern, 'animal', text)
print("Replaced text:", replaced_text)
pattern2 = r'\b\w{3}\b'  
matches2 = re.findall(pattern2, text)
print("Three-letter words found:", matches2)
splitted_text = re.split(r'\s+', text)  
print("Splitted text:", splitted_text)
capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', text)
print("Capitalized words:", capitalized_words)
