// 50.2.1
let fac_seq n = seq {
    let mutable factorial = 1
    for i in 0..n do
        factorial <- 1
        for j in 1..i do
            factorial <- factorial * j
        yield factorial
}

// 50.2.2
let seq_seq n = seq {
    for i in 0..n do
        if i % 2 = 0 then yield i/2
        else yield -(i + 1)/2
}