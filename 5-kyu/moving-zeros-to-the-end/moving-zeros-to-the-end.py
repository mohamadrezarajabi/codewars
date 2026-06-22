def move_zeros(lst):
    zero_count = 0
    result = []
    for num in lst:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1
    for zero in range(zero_count):
        result.append(0)
    return result