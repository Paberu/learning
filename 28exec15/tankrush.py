def TankRush(h1, w1, s1, h2, w2, s2):
    if s1 == '' or s2 == '' or h1 == 0 or h2 == 0 or w1 == 0 or w2 == 0:
        return False
    
    map1 = []
    s1 = s1.split()
    for i in range(h1):
        map1.append(list(s1[i]))

    map2 = []
    s2 = s2.split()
    for i in range(h2):
        map2.append(list(s2[i]))

    for i in range(0, h1-h2+1):
        for j in range(0, w1-w2+1):
            map_temp = [[map1[col][row] for row in range(i, i+h2)] for col in range(j, j+w2)]
            if map_temp == map2:
                return True

    return False


print(TankRush(4, 4, '1234 2345 0987 3562', 2, 2, '34 98'))
print(TankRush(4, 4, '1234 2345 0987 3562', 4, 4, '1234 2345 0987 3562'))
print(TankRush(2, 2, '34 98', 2, 2, '34 98'))
