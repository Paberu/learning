type F = 
  | AM
  | PM
  
type TimeOfDay = {hours: int; minutes: int; f: F}

let (.>.) (x:TimeOfDay) (y:TimeOfDay) =
    if x.f = AM && y.f = PM then false
    elif x.f = PM && y.f = AM then true
    else
        if x.hours > y.hours then true
        elif x.hours < y.hours then false
        else
            if x.minutes > y.minutes then true
            else false