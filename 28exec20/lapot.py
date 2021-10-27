file = ''
history = []
position = 0

def BastShoe(command):
    global file, history, position, last_command
    #print('----->',file)
    #print('----->',history)
    s = file

    if command[0] in ('1', '2', '3'):
        operation, parameter = command.split(maxsplit=1)
    else:
        operation = command[0]

    if operation in ('1', '2'):
        if operation == '1':
            s += parameter
        else: # operation == '2'
            index = int(parameter)
            if index:
                s = s[:-index]
        file = s
        history.append((command, file))
        position = len(history) - 1
        return s
    elif operation == '3':
        index = int(parameter)
        if index < len(s):
            return s[index]
        else:
            return ''
    elif operation == '4':
        if history[position][0][0] in ('1', '2'):
            position -= 1
            if position < 0:
                position = 0
            s = file = history[position][1]
        return s
    elif operation == '5':
        if history[position][0][0] in ('1', '2'):
            position += 1
            if position >= len(history):
                position = len(history) - 1
            s = file = history[position][1]
        return s
    else:
        return s


print(BastShoe('1 Привет'))
print(BastShoe('1  , Мир!'))
print(BastShoe('1 ++'))
print(BastShoe('2 2'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('1 *'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('3 6'))
print(BastShoe('2 100'))

print(BastShoe('1 Привет'))
print(BastShoe('1  , Мир!'))
print(BastShoe('1 ++'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('5'))
print(BastShoe('4'))
print(BastShoe('5'))
print(BastShoe('5'))
print(BastShoe('5'))
print(BastShoe('5'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('2 2'))
print(BastShoe('4'))
print(BastShoe('5'))
print(BastShoe('5'))
print(BastShoe('5'))
