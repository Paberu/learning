def madMax(n, tele):
    min_value, max_value = 0, max(tele)
    inter = [0]*n
    inter[int((n-1)/2)] = max_value
    tele.remove(max_value)
    for i in range(int((n - 1) / 2)):
        min_value = min(tele)
        inter[i] = min_value
        tele.remove(min_value)
    for i in range(int((n - 1) / 2)):
        max_value = max(tele)
        inter[int((n-1)/2)+i+1] = max_value
        tele.remove(max_value)
    return inter
