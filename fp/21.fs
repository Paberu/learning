// 50.2.1
let fac_seq n = seq {
    let mutable fact = 1
    for i in 1..n do
        fact <- fact * i
        yield fact
}

// 50.2.2
let seq_seq n = seq {
    for i in 0..n do
        if i % 2 = 0 then yield i/2
        else yield -(i + 1)/2
}
