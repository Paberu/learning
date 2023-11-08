let rec factorial n acc = 
    match n with
    | 0 | 1 -> acc
    | n -> factorial (n - 1) acc*n

// 50.2.1
let fac_seq n = seq {
    for i in 0..n do
        yield factorial i 1
}

// 50.2.2
let seq_seq n = seq {
    for i in 0..n do
        if i % 2 = 0 then yield i/2
        else yield -(i + 1)/2
}
