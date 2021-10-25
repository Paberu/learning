def BastShoe(command):
    s = ''
    operation = command[0]
    if operation == 1:
        s += command[2::]
    elif operation == 2:
        count = command.split()[1]

    elif operation == 3:

    elif operation == 4:

    elif operation == 5:

    else:
        return ''

print(BastShoe())