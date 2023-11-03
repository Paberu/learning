let try_find key m = 
    let rec look_through inner_key key_list =
        match key_list with
        | [] -> None
        | x::tail when x = inner_key -> Some(Map.find x m)
        | _::tail -> look_through inner_key tail
    look_through key (Map.keys m)

let map1 = Map.ofList [(128,"oksana"); (32,"oleg")]

let try_find key m = 
    if Map.containsKey key m then Some(Map.find key m)
    else None
	
	
printfn "%A" (try_find 32 map1)
printfn "%A" (try_find 23 map1)
printfn "%A" (try_find 32 map2)