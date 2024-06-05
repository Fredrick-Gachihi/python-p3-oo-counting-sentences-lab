#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        modified_value = self.value.replace(',', '.')
        sentences = modified_value.split('.')
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
    
