def white_walkers(village):
    start_num = -1
    white_walkers_count = 0
    for folk in village:
        if folk == '=':
            if start_num == -1:
                return False
            else:
                if white_walkers_count >= 3:
                    return False
                else:
                    white_walkers_count += 1
        elif folk.isdecimal():
            if white_walkers_count == 0:
                start_num = int(folk)
            else:
                finish_num = int(folk)
                if finish_num + start_num == 10:
                    if white_walkers_count not in (0, 3):
                        return False
                    else:
                        white_walkers_count = 0
                        start_num = finish_num
                else:
                    if white_walkers_count != 0:
                        return False
                    else:
                        start_num = finish_num

    if white_walkers_count != 0:
        return False
    else:
        return True


print(white_walkers("axxb6===4xaf5===eee5"))
print(white_walkers("5==ooooooo=5=5"))
print(white_walkers("abc=7==hdjs=3gg1=======5"))
print(white_walkers("aaS=8"))
print(white_walkers("9===1===9===1===9"))
