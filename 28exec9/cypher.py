def TheRabbitsFoot(s, encode):
    if encode:
        s = s.replace(' ','')
        size = len(s)**0.5
        rows = int(size)
        columns = rows + 1
        if rows * columns < len(s):
            rows += 1
        print(rows,' x ',columns)
        s_matrix = [''] * rows
        for i in range(rows):
            s_matrix[i] = ['']*columns
        print(s_matrix)
        for i in range(rows):
            for j in range(columns):
                if i*columns + j < len(s):
                    s_matrix[i][j] = s[i*columns+j]
                else:
                    break
        print(s_matrix)
        reverted_s = [[s_matrix[j][i] for j in range(rows)] for i in range(columns)]
        print(reverted_s)
        s = ' '.join(''.join(x) for x in reverted_s)
    else:
        pass
    return s

print(TheRabbitsFoot('отдай мою кроличью лапку', True))
