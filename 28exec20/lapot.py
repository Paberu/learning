file = ''
history = []
position = 0
last_operation = ''


def BastShoe(command):
    global file, history, position, last_operation
    s = file

    if command[0] in ('1', '2', '3'):
        operation, parameter = command.split(maxsplit=1)
    else:
        operation = command[0]

    if operation in ('1', '2'):
        if operation == '1':
            s += parameter
        else:  # operation == '2'
            index = int(parameter)
            if index:
                s = s[:-index]
        if last_operation == '4':
            history = []
            history.append(file)
        file = s
        history.append(file)
        position = len(history) - 1
        last_operation = operation
        return s
    elif operation == '3':
        index = int(parameter)
        last_operation = operation
        if index < len(s):
            return s[index]
        else:
            return ''
    elif operation == '4':
        position -= 1
        if position < 0:
            position = 0
        s = file = history[position]
        last_operation = operation
        return s
    elif operation == '5':
        position += 1
        if position >= len(history):
            position = len(history) - 1
        s = file = history[position]
        last_operation = operation
        return s
    else:
        return s
