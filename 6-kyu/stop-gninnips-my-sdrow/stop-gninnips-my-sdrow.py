def spin_words(sentence):
    spl = sentence.split(" ")
    for i,word in enumerate(spl):
        if len(word) >= 5:
            spl[i] = word[::-1]
    return " ".join(spl)