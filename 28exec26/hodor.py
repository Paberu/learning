def white_walkers(village):
    start_num = -1
    white_walkers_count = 0
    found = False
    for folk in village:
        if folk == '=':
            white_walkers_count += 1
        elif folk.isdecimal():
            if start_num == -1:
                start_num = int(folk)
                white_walkers_count = 0
            else:
                finish_num = int(folk)
                if finish_num + start_num == 10:
                    if white_walkers_count not in (0, 3):
                        return False
                    elif white_walkers_count == 3:
                        white_walkers_count = 0
                        start_num = finish_num
                        found = True
                    else:
                        start_num = finish_num
                else:
                    white_walkers_count = 0
                    start_num = finish_num
    return found
