def TreeOfLife(h, w, n, tree):
    tree_array = [''] * h
    for i in range(h):
        tree_array[i] = list(tree[i])

    for i in range(h):
        for j in range(w):
            if tree_array[i][j] == '.':
                tree_array[i][j] = 0
            elif tree_array[i][j] == '+':
                tree_array[i][j] = 1
            else:
                return IOError

    coordinates_for_deletion = []
    for year in range(n):
        for i in range(h):
            for j in range(w):
                tree_array[i][j] += 1
        if year % 2 != 0:
            for i in range(h):
                for j in range(w):
                    if tree_array[i][j] >= 3:
                        coordinates_for_deletion.append((i, j))
                        if i > 0:
                            coordinates_for_deletion.append((i-1, j))
                        if j > 0:
                            coordinates_for_deletion.append((i, j-1))
                        if i < h - 1:
                            coordinates_for_deletion.append((i+1, j))
                        if j < w - 1:
                            coordinates_for_deletion.append((i, j+1))
            for every_coordinate in coordinates_for_deletion:
                tree_array[every_coordinate[0]][every_coordinate[1]] = 0
        coordinates_for_deletion.clear()

    for i in range(h):
        for j in range(w):
            if tree_array[i][j] == 0:
                tree_array[i][j] = '.'
            else:
                tree_array[i][j] = '+'
    for i in range(h):
        tree_array[i] = ''.join(tree_array[i])

    return tree_array
