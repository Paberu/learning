def TheRabbitsFoot(s, encode):
    s = s.replace(' ','')
    size = len(s)**0.5
    rows = int(size)
    columns = rows + 1
    if rows * columns < len(s):
        rows += 1
    print(rows,' x ',columns)
    new_s = ''
    for i in range(columns):
        for j in range(rows):
            new_s = 
    return s

print(TheRabbitsFoot('отдай мою кроличью лапку', True))
