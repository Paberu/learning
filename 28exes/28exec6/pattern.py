def PatternUnlock(N, hits):
    result = []
    path = 0
    diag_nums = ((2, 4), (4, 2), (2, 6), (6, 2), (2, 9), (9, 2), (2, 7), (7, 2))
    for i in range(N-1):
        if (hits[i], hits[i+1]) not in diag_nums:
            path += 1
        else:
            path += 2**0.5
    for symbol in str(round(path, 5)):
        if symbol not in ('0', '.'):
            result.append(symbol)
    return ''.join(result)
