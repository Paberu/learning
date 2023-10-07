let curry f = 
    let g x =
	    let h y = 
		    f (x,y)
			
let uncurry g = 
    let f (x,y) = 
	    let h y = 
		    let g x
