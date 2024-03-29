// 40.1
let sum(p, xs) = 
    let rec check (p, xs, result) =
        match xs with
        | x::tail when p x -> check(p, tail, result + x)
        | _::tail -> check(p, tail, result)
        | [] -> result
    check (p, xs, 0)
  
// 40.2.1
let rec count (xs, n) =
    match xs with
    | [] -> 0
    | x::tail when x < n -> count(tail, n)
    | x::tail when x = n -> 1 + count(tail, n)
    | _ -> 0
 
 // 40.2.2
let rec insert (xs, n) = 
    match xs with
    | [] -> n::[]
    | x::tail when x < n -> x :: insert(tail,n)
    | x::tail -> n :: x :: tail
 
// 40.2.3
let rec intersect (xs1, xs2) =
    match xs1, xs2 with
    | [], _ -> []
    | _, [] -> []
    | x1::tail1, _ when x1 < List.head xs2 -> intersect(tail1, xs2)
    | _, x2::tail2 when List.head xs1 > x2 -> intersect(xs1, tail2)
    | x1::tail1, x2::tail2 when x1 = x2 -> x1 :: intersect(tail1, tail2)

    
//40.2.4
let rec plus (xs1, xs2) = 
    match xs1, xs2 with
    | [], _ -> xs2
    | _, [] -> xs1
    | xs1, x2::tail2 -> plus(insert(xs1, x2), tail2)

let rec remove (xs, n) =
    match xs with
    | [] -> []
    | x::tail when x < n -> x :: remove(tail,n)
    | x::tail when x = n -> tail
    | tail -> tail

// 40.2.5
let rec minus (xs1, xs2) = 
    match (xs1, xs2) with
    | [], _ -> []
    | xs1, [] -> xs1
    | _, x2::tail2 -> minus(remove(xs1, x2), tail2)

// 40.3.1
let rec smallest = function
    | [] -> None
    | x::tail -> 
        let rec check(xs, minimal) = 
            match xs with
            | [] -> Some minimal
            | x::tail when x < minimal -> check(tail, x)
            | x::tail -> check(tail, minimal)
        check(tail, x)
    
// 40.3.2
let rec delete (n, xs) =
    match xs with
    | [] -> []
    | x::tail when x=n -> tail
    | x::tail -> x::delete(n, tail)
    
// 40.3.3
let rec sort = function
    | [] -> []
    | xs ->
        let minimal = Option.get (smallest xs)
        minimal::sort(delete(minimal, xs))


let rec reverseList acc xs =
    match xs with
    | [] -> acc
    | x::tail -> reverseList (x::acc) tail

let rec reverseInnerLists = function
    | [] -> []
    | x :: tail -> (reverseList [] x) :: reverseInnerLists tail

// 40.4   
let revrev xs = reverseList [] (reverseInnerLists xs)
