let checkWallet (w: int*int*int) = 
    let g, s, c = w
    let totalCopper = ((g * 20 + s) * 12) + c
    let g = totalCopper / 240
    let s = (totalCopper % 240) / 12
    let c = (totalCopper % 240) % 12
    (g, s, c)

// 23.4.1
let (.+.) x y = 
    let g1, s1, c1 = x
    let g2, s2, c2 = y
    let g = g1 + g2
    let s = s1 + s2
    let c = c1 + c2
    let wallet = (g, s, c)
    let wallet = checkWallet wallet
    wallet
    
let (.-.) x y = 
    let g1, s1, c1 = x
    let g2, s2, c2 = y
    let g = g1 - g2
    let s = s1 - s2
    let c = c1 - c2
    let wallet = (g, s, c)
    let wallet = checkWallet wallet
    wallet
 
// 23.4.2
let (.+) (x:float*float) (y:float*float) = 
    let (a, b) = x
    let (c, d) = y
    (a + c, b + d)
   
let (.*) (x:float*float) (y:float*float) = 
    let (a, b) = x
    let (c, d) = y
    (a*c - b*d, b*c + a*d)

let (.-) (x:float*float) (y:float*float) = 
    let (a, b) = y
    (.+) x (-a, -b)
    
let (./) (x:float*float) (y:float*float) = 
    let (a, b) = y
    let antiY = (a/(a*a+b*b),-b/(a*a+b*b))
    (.*) x antiY
