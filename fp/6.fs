// 17.1
let rec pow : string * int -> string = function
    |(s,0) -> ""
    |(s,1) -> s
    |(s,n) -> s+pow(s,n-1)

// 17.2
let rec isIthChar : string * int * char -> bool = function
    |(s,n,c) when n >= 0 && n < String.length(s) -> s.[n] = c
    |_ -> false

// 17.3
let rec countChar : string * int * char * int -> int = function
    |(str,position,ch,total) when position = String.length(str) -> total
    |(str,position,ch,total) when isIthChar(str,position,ch) -> countChar(str,position+1,ch,total+1)
    |(str,position,ch,total) -> countChar(str,position+1,ch,total)

let rec occFromIth : string * int * char -> int = function
    |(s,n,c) -> countChar(s,n,c,0)