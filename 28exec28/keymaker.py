def Keymaker(k):
    doors = [False]*k
    for i in range(k):
        for j in range(k):
            if (j+1) % (i+1) == 0:
                doors[j] = not doors[j]

    return ''.join(['1' if door else '0' for door in doors])
