// 42.3
let rec allSubsets n k =
    let createBasicSet n =
        let rec generateSubSets (acc:Set<Set<int>>) = function
            | 0 -> acc
            | x -> generateSubSets (Set.union acc (Set.map (Set.add x) acc)) (x-1)
        generateSubSets (Set.singleton Set.empty) n
    
    let subsets = createBasicSet n
    subsets |> Set.filter (fun subset -> subset.Count = k)


printfn "%A" (allSubsets 9 0)