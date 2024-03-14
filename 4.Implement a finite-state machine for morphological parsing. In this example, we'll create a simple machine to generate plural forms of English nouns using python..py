class PluralFSM:
    def __init__(self):
        self.transitions = {
            'S': {'consonant': 'ES', 'vowel': 'S'},
            'ES': {'consonant': 'IES', 'vowel': 'ES'},
            'IES': {'consonant': 'S', 'vowel': 'ES'}
        }
        self.initial_state = 'S'
        self.final_states = {'S', 'ES', 'IES'}
    def generate_plural(self, noun):
        state = self.initial_state
        last_char = noun[-1]

        if last_char in 'aeiouAEIOU':
            last_char_type = 'vowel'
        else:
            last_char_type = 'consonant'

        for char in reversed(noun):
            if state in self.transitions:
                next_state = self.transitions[state][last_char_type]
                state = next_state
            else:
                return None

        if state in self.final_states:
            if state == 'S':
                return noun + 's'
            elif state == 'ES':
                return noun + 'es'
            elif state == 'IES':
                return noun[:-1] + 'ies'
        else:
            return None
if __name__ == "__main__":
    fsm = PluralFSM()
    
    nouns = ['cat', 'dog', 'fox', 'baby', 'woman', 'man', 'child', 'person', 'knife', 'leaf', 'city']
    for noun in nouns:
        plural_form = fsm.generate_plural(noun)
        print(f"{noun}: {plural_form}")
