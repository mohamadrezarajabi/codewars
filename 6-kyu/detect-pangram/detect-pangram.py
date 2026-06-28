def is_pangram(st):
    st = st.lower()
    
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in st:
            return False
    return True