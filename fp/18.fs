// 47.4.1
let f (n:int):int = 
    let factorial = ref 1
    let mutable x = 1
    while x <= n do
        factorial := ! factorial * x
        x <- x + 1
    ! factorial

// 47.4.2
let fibo (n:int):int = 
    let mutable f1 = 0
    let mutable f2 = 1
    for _ in 1..n do
        let temp = f1
        f1 <- f2
        f2 <- temp + f2
    f1
    
printfn "%d" (fibo 4)