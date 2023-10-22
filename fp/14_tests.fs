        
let testFun x = x > 0
printfn "%d" (sum(testFun, [-3;-2;-1;0;1;2;3]))
printfn "%d" (sum(testFun, [-3;-2;-1]))
printfn "%d" (sum(testFun, []))

printfn "%d" (count ([], 5))
printfn "%d" (count ([5;5;5;5], 5))
printfn "%d" (count ([1;2;3;4], 5))
printfn "%d" (count ([11;12;13;14], 5))

printfn "%A" (insert ([], 5))
printfn "%A" (insert ([1;2;4;5], 3))
printfn "%A" (insert ([1;2;3;4], 0))
printfn "%A" (insert ([11;12;13;14], 15))

printfn "%A" (intersect ([1;2;3;4;5],[3;4;5;6;7]))
printfn "%A" (intersect ([],[3;4;5;6;7]))
printfn "%A" (intersect ([1;2;3;4;5],[]))
printfn "%A" (intersect ([1;2;3;4;5],[6;7;8;9]))
printfn "%A" (intersect ([1;2;3;4;5],[5;6;7;8;9]))
printfn "%A" (intersect ([1;3;3;4;4;5;5;7;9],[3;4;4;4;4;5;5;6;7;8;9]))

printfn "%A" (plus ([1;2;3;4;5],[]))
printfn "%A" (plus ([],[3;4;5;6;7]))
printfn "%A" (plus ([1;2;3;4;5],[3;4;5;6;7]))
printfn "%A" (plus ([1;2;3;4;5],[6;7;8;9]))
printfn "%A" (plus ([4;5;5],[5;5;6]))
printfn "%A" (plus ([1;3;5;7;9;11],[0;2;4;6;8;10;12]))

printfn "%A" (minus ([1;2;3;4;5],[]))
printfn "%A" (minus ([],[3;4;5;6;7]))
printfn "%A" (minus ([1;2;3;4;5],[3;4;5;6;7]))
printfn "%A" (minus ([1;2;3;4;5],[6;7;8;9]))
printfn "%A" (minus ([4;5;5],[5;5;6]))
printfn "%A" (minus ([1;3;5;7;9;11],[0;2;4;6;8;10;12]))

printfn "%A" (smallest ([]))
printfn "%A" (smallest ([3;4;5;6;7]))
printfn "%A" (smallest ([5;2;5;1;5;1;3]))
printfn "%A" (smallest ([2;2;2;2;2]))

printfn "%A" (delete (1,[]))
printfn "%A" (delete (2,[3;4;5;6;7]))
printfn "%A" (delete (5,[5;2;5;1;5;1;3]))
printfn "%A" (delete (2,[2;2;2]))

printfn "%A" (sort ([]))
printfn "%A" (sort ([3;4;5;6;7]))
printfn "%A" (sort ([5;2;5;1;5;1;3]))
printfn "%A" (sort ([2;2;2]))

printfn "%A" (revrev ([]))
printfn "%A" (revrev ([[3;4;5;6;7];[]]))
printfn "%A" (revrev ([[5;2];[5;1];[5;1;3]]))
printfn "%A" (revrev ([[2];[2;2]]))