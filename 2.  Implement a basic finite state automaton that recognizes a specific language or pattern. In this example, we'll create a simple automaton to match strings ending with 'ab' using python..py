class FSA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'a', 'b'}        
        self.transitions = {            
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q0',
        }
        self.start_state = 'q0'           
        self.accept_states = {'q2'}       

    def run(self, string):
        current_state = self.start_state
        for char in string:
            if (current_state, char) in self.transitions:
                current_state = self.transitions[(current_state, char)]
            else:
                return False
        return current_state in self.accept_states
automaton = FSA()
strings = ["ab", "aab", "aba", "abb", "aabb", "b", "a"]
for string in strings:
    if automaton.run(string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")
