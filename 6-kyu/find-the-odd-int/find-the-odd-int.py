def find_it(seq):        
    return next(num for num in seq if seq.count(num) % 2 == 1)