def odometer(oksana):
    s = 0
    t = 0
    for i in range(0, len(oksana), 2):
        s += oksana[i] * (oksana[i+1] - t)
        t = oksana[i+1]
    return s
