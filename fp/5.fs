// 16.1
let notDivisible : int * int -> bool = function
    |(n,m) when n = 0 -> false
    |(n,m) -> (m % n = 0)

// 16.2
let prime (n: int) : bool =
    let rec check : int -> bool = function
        |i when i = 2 -> n % 2 <> 0 && check (i + 1)
        |i -> i > n/2 || (n % i <> 0 && check (i + 2))
    check 2
