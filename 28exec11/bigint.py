def BigMinus(s1, s2):
    if s1 < s2:
        s1, s2 = s2, s1
    temp_len = len(s1) - len(s2)
    temp_res = list(map(int, s1[:temp_len]))
    calculated_res = [0]*len(s2)
    debt = 0
    for i in range(-1, -len(s2)-1, -1):
        int1 = int(s1[i])
        int2 = int(s2[i])
        if int1 < int2:
            int_res = 10 + int1 - int2 - debt
            debt = 1
        else:
            int_res = int1 - int2 - debt
            debt = 0
        calculated_res[i] = int_res
    if debt:
        temp_res[-1] -= 1

    res = temp_res + calculated_res
    leading_zeros = 0
    for i in range(len(res)-1):
        if res[i] == 0:
            leading_zeros += 1
        else:
            break

    return ''.join(map(str, res[leading_zeros:]))
