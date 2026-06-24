def digital_root(n):
    while n >= 10:
        sum = 0
        for digit in str(n):
            sum += int(digit)
        n = sum
    return n