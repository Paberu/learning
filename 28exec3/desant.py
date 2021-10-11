def ConquestCampaign(N, M, L, battalion):

    country = [0] * N
    for i in range(N):
        country[i] = [0]*M
    day = 1
    noZeros = False
    for i in range(0, L*2, 2):
        country[battalion[i]-1][battalion[i+1]-1] = 1

    while not noZeros and day < 9:
        for i in range(N):
            for j in range(M):
                if country[i][j] != 0:
                    country[i][j] += 1

        for i in range(N):
            for j in range(M):
                if country[i][j] == 2:
                    if i > 0 and country[i-1][j] == 0:
                        country[i-1][j] += 1
                    if j > 0 and country[i][j-1] == 0:
                        country[i][j-1] += 1
                    if i < N-1 and country[i+1][j] == 0:
                        country[i+1][j] += 1
                    if j < M-1 and country[i][j+1] == 0:
                        country[i][j+1] += 1

        for i in range(N):
            print(country[i])

        day += 1
        if not any(0 in row for row in country):
            noZeros = True

    return day

print(ConquestCampaign(3, 4, 2, [2, 2, 3, 4]))
