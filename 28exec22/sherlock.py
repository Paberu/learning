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

    if len(check_numbers.values()) == 1:
        return True
    elif len(check_numbers.values()) > 2:
        return False
    else:  # len == 2
        if check_numbers[1] == 1:
            return True
        elif 2 in check_numbers.keys():
            if check_numbers[1] > 1 and check_numbers[2] == 1:
                return True
            else:
                return False
        else:
            return False
