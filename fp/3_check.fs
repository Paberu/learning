//F# Compiler for F# 4.0 (Open Source Edition)

open System
let days_in_month : int -> int = function
    |1|3|5|7|8|10|12 -> 31
    |4|6|9|11 -> 30
    |2 -> 28
    |_ -> 0

printfn "%d" (days_in_month(5))
printfn "%d" (days_in_month(15))
printfn "%d" (days_in_month(2))
printfn "%d" (days_in_month(4))
printfn "%d" (days_in_month(7))
