from functools import reduce

lst = [15,1,25,2,30,3,10,5]
time = lst[1::2]
speed = lst[0::2]

time_hours = [end - begin for end, begin in zip(time, [0, *time[:-1]])]
distance = reduce(lambda a,b: a+b, [hours * velosity for hours, velosity in zip(time_hours, speed)])
