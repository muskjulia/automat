import json

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def make_state(dictionary):
    if not dictionary:
        return {}
    state = {}
    for letter in alphabet:
        sub_dict = filter(lambda word: word.startswith(letter), dictionary)
        sub_dict = list(map(lambda word: word[1:], sub_dict))
        if sub_dict: # delete this validation for the sake of more saturated state machine
            state[letter] = make_state(sub_dict)
    return state


words = []
with open('dict.txt', 'r') as f:
    words = f.read()
    words = words.split()
 
automat = make_state(words)

with open('result.json', 'w') as f:
    print(str(automat).replace('\'', '\"'))
    f.write(str(automat).replace('\'', '\"'))