def TheRabbitsFoot(s, encode):
    if encode:
        s = s.replace(' ', '')
        size = len(s)**0.5
        rows = int(size)
        columns = rows + 1
        if rows * columns < len(s):
            rows += 1
            
        s_matrix = [''] * rows
        for i in range(rows):
            s_matrix[i] = ['']*columns
            
        for i in range(rows):
            for j in range(columns):
                if i*columns + j < len(s):
                    s_matrix[i][j] = s[i*columns+j]
                else:
                    break
        reverted_s = [[s_matrix[j][i] for j in range(rows)] for i in range(columns)]
        s = ' '.join(''.join(x) for x in reverted_s)
    else:
        #s = s.replace(' ', '')
        size = len(s)**0.5
        columns = int(size)
        rows = columns + 1
        if rows * columns < len(s):
            columns += 1
            
        s_matrix = [''] * rows
        for i in range(rows):
            s_matrix[i] = ['']*columns

        for i in range(rows):
            for j in range(columns):
                if i * columns + j < len(s):
                    s_matrix[i][j] = s[i*columns+j]
                else:
                    s_matrix[i][j] = ''

        reverted_s = [[s_matrix[j][i] for j in range(rows)] for i in range(columns)]
        s = ''.join(''.join(x) for x in reverted_s)

    return s


print(TheRabbitsFoot('ahe so sl', False))
##print(TheRabbitsFoot('asshole', True))
##print(TheRabbitsFoot('отдай мою кроличью лап', True))
##print(TheRabbitsFoot('омоютоллдюиаакчпйрь', False))
##
##print(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False))
##print(TheRabbitsFoot('отдай мою кроличью лапку', True))
