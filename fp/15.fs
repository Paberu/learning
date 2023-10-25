// 41.4.1
let list_filter f xs =
    List.foldBack(fun x acc -> if f x then x::acc else acc) xs []
    

// 41.4.2
let sum (p, xs) =
    List.fold(fun x acc -> if p x then x + acc else acc) 0 xs

// 41.4.3
let rev lst = List.fold (fun head tail -> tail::head) [] lst

let revrev lst = List.fold (fun head tail -> rev tail::head) [] lst