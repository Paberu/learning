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
        parts = s.split()
        columns = len(parts[0])
        rows = len(parts)
        if rows * columns < len(s.replace(' ', '')):
            columns += 1
        s_matrix = [''] * rows
        for i in range(rows):
            s_matrix[i] = ['']*columns
        for i in range(columns):
            for j in range(rows):
                s_matrix[j][i] = parts[j][i] if i < len(parts[j]) else ''
        reverted_s = [[s_matrix[j][i] for j in range(rows)] for i in range(columns)]
        s = ''.join(''.join(x) for x in reverted_s)
    return s

print(TheRabbitsFoot('однажды в студеную зимнюю порру', True))
print(TheRabbitsFoot('оыемр двннр нсуюу атюю жузп ддио', False))
print(TheRabbitsFoot('а б абв', True))
print(TheRabbitsFoot('аб бв а', False))

print(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False))
print(TheRabbitsFoot('отдай мою кроличью лапку', True))