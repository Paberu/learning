// 50.2.1
let rec factorial n acc = 
    match n with
    | 0 | 1 -> acc
    | n -> factorial (n - 1) acc*n
    
let rec fac_seq_gen i =
    seq {
        yield factorial i 1
        yield! fac_seq_gen (i + 1)
    }

let fac_seq = seq {
    yield! fac_seq_gen 0
}

// 50.2.2
let rec f i= seq {
    yield (0 - i)
    yield i
    yield! f(i + 1)
}

let seq_seq = seq {
    yield 0
    yield! f 1
}