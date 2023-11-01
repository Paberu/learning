let try_find key m = 
    let rec look_through inner_key key_list =
        match key_list with
        | [] -> None
        | x::tail when x = inner_key -> Some(Map.find x m)
        | _::tail -> look_through inner_key tail
    look_through key (Map.keys m)

