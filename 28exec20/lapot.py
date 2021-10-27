file = ''
history = []
position = 0
last_operation = ''

def BastShoe(command):
    global file, history, position, last_operation
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


print(1,BastShoe('1 Привет'))
print(2,BastShoe('1  , Мир!'))
print(3,BastShoe('1 ++'))
print(4,BastShoe('2 2'))
print(5,BastShoe('4'))
print(6,BastShoe('4'))
print(7,BastShoe('1 *'))
print(8,BastShoe('4'))
print(9,BastShoe('4'))
print(10,BastShoe('4'))
print(11,BastShoe('3 6'))
print(12,BastShoe('2 100'))

print(13,BastShoe('1 Привет'))
print(14,BastShoe('1  , Мир!'))
print(15,BastShoe('1 ++'))
print(16,BastShoe('4'))
print(17,BastShoe('4'))
print(18,BastShoe('5'))
print(19,BastShoe('4'))
print(20,BastShoe('5'))
print(21,BastShoe('5'))
print(22,BastShoe('5'))
print(23,BastShoe('5'))
print(24,BastShoe('4'))
print(25,BastShoe('4'))
print(26,BastShoe('2 2'))
print(27,BastShoe('4'))
print(28,BastShoe('5'))
print(29,BastShoe('5'))
print(30,BastShoe('5'))
