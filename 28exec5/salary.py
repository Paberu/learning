def SynchronizingTables(N, ids, salary):

    salary_result = [0]*N
    for i in range(N):
        salary_result[sorted(ids).index(ids[i])] = sorted(salary)[i]
    return salary_result
