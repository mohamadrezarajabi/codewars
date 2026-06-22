def pig_it(text):
    sentence = text.split(" ")
    result = []
    for word in sentence:
        if not word.isalpha():
            result.append(word)
            continue
        else:
            first_word = word[0]
            other_word = word[1:]
            new_word = f"{other_word}{first_word}ay"
            result.append(new_word)
    return " ".join(result)