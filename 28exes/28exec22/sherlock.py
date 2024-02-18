def SherlockValidString(s):
    counter = dict()
    for letter in s:
        if letter not in counter.keys():
            counter[letter] = 1
        else:
            counter[letter] += 1

    check_numbers = dict()
    for number in counter.values():
        if number not in check_numbers.keys():
            check_numbers[number] = 1
        else:
            check_numbers[number] += 1

    keys = check_numbers.keys()
    if len(keys) == 1:
        return True
    elif len(keys) == 2:
        if min(keys) == max(keys) - 1:
            if check_numbers[max(keys)] == 1:
                return True
        if 1 in keys:
            if check_numbers[1] == 1:
                return True

    return False
