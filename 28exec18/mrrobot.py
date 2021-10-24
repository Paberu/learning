def MisterRobot(n, data):
    while n:
        while n == data[n-1]:
            data.pop()
            n -= 1
            if not n:
                return True

        piece_of_data = data[-3::]
        while not piece_of_data[0] < piece_of_data[1] < piece_of_data[2]:
            piece_of_data.append(piece_of_data.pop(0))
            if piece_of_data == data[-3::]:
                return False
        data = data[0:-3]+piece_of_data
