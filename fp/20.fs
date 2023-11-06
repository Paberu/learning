// 49.5.1
let even_seq = Seq.initInfinite (fun i -> 2*i + 2)

// 49.5.2
let fac_seq = 
    let rec factorial n acc = 
        match n with
        | 0 | 1 -> acc
        | n -> factorial (n - 1) acc*n
    Seq.initInfinite (fun i -> factorial i 1)

// 49.5.3
let seq_seq = 
    Seq.initInfinite (fun i ->
            if i % 2 = 0 then i/2
            else -(i + 1)/2
        )