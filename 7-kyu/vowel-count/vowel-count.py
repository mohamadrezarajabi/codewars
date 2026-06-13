# def get_count(sentence):
#     vowels = "aeiou"
#     count = 0
#     for letter in sentence:
#         for _ in vowels:
#             if _ == letter:
#                 count += 1
#     return count
​
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for letter in sentence:
        if letter in vowels:
                count += 1
    return count