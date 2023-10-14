let upto n = 
    let rec raise = function
        | (0, acc) -> []
        | (1, acc) -> 1::acc
        | (n, acc) -> raise(n-1, n::acc)
    raise(n, [])
 
 
let dnto n =
    let rec low = function
        | (k, acc) when k = 0 -> []
        | (k, acc) when k = n -> k::acc
        | (k, acc) -> low(k+1, k::acc)
    low(1, [])    

    
let rec evenn n = 
    let rec addTwo = function
        | (0, acc) -> acc
        | (k, acc) -> addTwo(k-1, (k-1)*2::acc)
    addTwo(n, [])