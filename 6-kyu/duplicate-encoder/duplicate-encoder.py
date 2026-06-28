def duplicate_encode(word):
    word = word.lower()
    
    result = "".join("(" if word.count(letter) == 1 else ")" for letter in word)
    
    return result
​
    #word = word.lower()
    #result = ""    
    #for letter in word:
        #if word.count(letter) == 1:
       #     result += "("
      #  else:
     #       result += ")"
    #return result
​
    