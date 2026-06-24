def disemvowel(text):
    total = ""
    for l in text:
        if l not in "aeiouAEIOU":
            total += l
    return total