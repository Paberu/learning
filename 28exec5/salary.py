def SynchronizingTables(N, ids, salary):

    sorted_ids = sorted(ids)
    sorted_salary = sorted(salary)
    unsorted_indexes = [0]*N

    for i in range(N):
        unsorted_indexes[i] = sorted_ids.index(ids[i])

    salary_result = [0]*N
    for i in range(N):
        salary_result[unsorted_indexes[i]] = sorted_salary[i]

    return salary_result


print(SynchronizingTables(5, [15,10,6,11,1], [1000,500,100,300,450]))
