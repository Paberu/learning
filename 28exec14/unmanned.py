def Unmanned(l, n, track):
    total_time = 0
    last_coordinate = 0
    for i in range(n):
        move_to_new_coordinate = track[i][0] - last_coordinate # time of movement (new coord - last coord)
        time_of_red = track[i][1]
        time_of_green = track[i][2]
        total_time += move_to_new_coordinate # previous time of movement + current time of movement
        remainder = total_time % (time_of_red+time_of_green) # when did it come?
        if remainder < time_of_red:                          # on red light or on green
            total_time += time_of_red - remainder
        last_coordinate = track[i][0]
    total_time += l - last_coordinate
    return total_time
