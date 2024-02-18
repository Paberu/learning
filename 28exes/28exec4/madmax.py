def MadMax(N, Tele):
    min_value, max_value = 0, max(Tele)
    inter = [0]*N
    inter[int((N-1)/2)] = max_value
    Tele.remove(max_value)
    for i in range(int((N - 1) / 2)):
        min_value = min(Tele)
        inter[i] = min_value
        Tele.remove(min_value)
    for i in range(int((N - 1) / 2)):
        max_value = max(Tele)
        inter[int((N-1)/2)+i+1] = max_value
        Tele.remove(max_value)
    return inter
