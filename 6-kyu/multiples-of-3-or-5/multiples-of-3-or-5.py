def solution(number):
    count = 0
    for digit in range(number):
        Divisibility_5 = digit % 5 == 0
        Divisibility_3 = digit % 3 == 0 
        if Divisibility_5 or Divisibility_3:
            count += digit
    return count 
​