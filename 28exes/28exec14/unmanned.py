def Unmanned(l, n, track):
    for i in range(n):
        if track[i][0] > l:
            fooled = True
        else:
            fooled = False
            break

    if not fooled:
        total_time = 0
        last_coordinate = 0
        for i in range(n):
            move_to_new_coordinate = track[i][0] - last_coordinate
            time_of_red = track[i][1]
            time_of_green = track[i][2]
            total_time += move_to_new_coordinate
            remainder = total_time % (time_of_red+time_of_green)
            if remainder < time_of_red:
                total_time += time_of_red - remainder
            last_coordinate = track[i][0]
        total_time += l - last_coordinate
        return total_time
    else:
        return l
