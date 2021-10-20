def TankRush(h1, w1, s1, h2, w2, s2):
<<<<<<< HEAD
    if s1 == '' or s2 == '' or h1 == 0 or h2 == 0 or w1 == 0 or w2 == 0:
        return False

=======
>>>>>>> parent of 6a92cd1 (Update tankrush.py)
    map1 = []
    s1 = s1.split()
    for i in range(h1):
        map1.append(list(s1[i]))

    map2 = []
    s2 = s2.split()
    for i in range(h2):
        map2.append(list(s2[i]))

    map_temp = [0]*h2
    for i in range(h2):
        map_temp[i] = [0]*w2

<<<<<<< HEAD
    return False
=======
    for i in range(0, h1-h2):
        for j in range(0, w1-w2):
            map_temp[0] = map[i]
           # print(map1[i:i+w2][j:j+w2])
            pass


print(TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98'))
>>>>>>> parent of 6a92cd1 (Update tankrush.py)
