// 39.1
let rec rmodd inputList =
    match inputList with
    | [] | [_] -> []
    | _ :: x :: tail -> x :: rmodd tail

// 39.2
let rec del_even inputList =
    match inputList with
    | [] -> []
    | x :: tail when x % 2 = 1 -> x :: del_even tail
    | _ :: tail -> del_even tail

// 39.3
let rec multiplicity x xs =
    let rec count = function
        | ([], element, accum) -> accum
        | (x :: tail, element, accum) when x = element -> count (tail, element, accum + 1)
        | (_ :: tail, element, accum) -> count (tail, element, accum)
    count (xs, x, 0)

// 39.4
let rec split = function
    | [] -> ([], [])
    | [x] -> ([x], [])
    | x1 :: x2 :: tail ->
        let (odds, evens) = split tail
        (x1 :: odds, x2 :: evens)

exception NotSameLength

// 39.5
let rec zip (xs1,xs2) =
    if  List.length xs1 <> List.length xs2 then 
        raise NotSameLength
    else
        match (xs1, xs2) with
            | ([],[]) -> []
            | (x1 :: tail1, x2 :: tail2) -> x1 :: x2 :: zip (tail1, tail2)