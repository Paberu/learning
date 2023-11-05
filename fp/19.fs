// 48.4.1
let rec fibo1 n n1 n2 =
    let rec f i fn1 fn2 = 
        if i > n then fn2
        else f (i + 1) (fn1+fn2) fn1
    f 1 n1 n2

// 48.4.2
let rec fibo2 n c =
    if n <= 1 then c n
    else fibo2 (n-1) (fun f1 -> fibo2 (n-2) (fun f2 -> c (f1 + f2)))

//48.4.3
let bigList n k =
    let rec loop n acc =
        if n = 0 then k acc
        else loop (n-1) (1::acc)
    loop n []
