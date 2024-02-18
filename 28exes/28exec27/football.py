def Football(f, n):
    down_count = []
    temp = []
    for i in range(1, n):
        if f[i] > f[i-1]:
            if len(temp):
                down_count.append(temp)
                temp = []
        else:
            if f[i-1] not in temp:
                temp.append(f[i-1])
            if f[i] not in temp:
                temp.append(f[i])
    if len(temp):
        down_count.append(temp)

    if len(down_count) == 1:
        return True
    elif len(down_count) == 2:
        return all(len(inner) == 2 for inner in down_count)
    else:
        return False

