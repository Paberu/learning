def SynchronizingTables(N, ids, salary):
    salary_result = [0]*N
    for i in range(N):
        salary_result[i] = sorted(salary)[sorted(ids).index(ids[i])]
    return salary_result
