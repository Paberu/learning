def squirrel(N):
    fact = 1
    for i in range(1, N+1):
        fact *= i
    n = int(str(fact)[0])
    return n
