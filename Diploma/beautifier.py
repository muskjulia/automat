with open('dict_new.txt', 'r') as f:
    with open('dict.txt', 'w') as new_dict: 
        words = f.read()
        words = words.split()
        words = list(set(words))
        words.sort()
        for word in words:
            new_dict.write(word + '\n')