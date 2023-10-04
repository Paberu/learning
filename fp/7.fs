// 20.3.1
let vat n x = x * (1.0 + (float n)/100.0)

// 20.3.2
let unvat n x = x / (1.0 + (float n)/100.0)

// 20.3.3
let rec min f = 
    let rec check x f = if f x = 0 then x else check (x+1) f
    check 1 f