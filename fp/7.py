def conquest_campaign(day, country):
    if not any(0 in row for row in country):
        return day
    else:
        n = len(country)
        m = len(country[0])
        for i in range(n):
            for j in range(m):
                if country[i][j] != 0:
                    country[i][j] += 1

        for i in range(n):
            for j in range(m):
                if country[i][j] == 2:
                    if i > 0 and country[i - 1][j] == 0:
                        country[i - 1][j] += 1
                    if j > 0 and country[i][j - 1] == 0:
                        country[i][j - 1] += 1
                    if i < n - 1 and country[i + 1][j] == 0:
                        country[i + 1][j] += 1
                    if j < m - 1 and country[i][j + 1] == 0:
                        country[i][j + 1] += 1
        return conquest_campaign(day+1, country)


width = 5
height = 4
units = 2
battalion = [2, 2, 4, 5]

country = [[0 for _ in range(width)] for _ in range(height)]

for i in range(0, units*2, 2):
    country[battalion[i]-1][battalion[i+1]-1] = 1


print(conquest_campaign(1, country))
