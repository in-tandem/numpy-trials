import numpy as np 

def execute():
    
    a = np.random.randint(1,3,(2,3))

    ##how to check if an array shares the same memory (ie a block)
    ## you call.base.. if you .base is NOne it is a copy else a view
    b = a[1:,:1]
    c = a[[1,1]] #fancy indexing..returns a copy..row1 returned twice
    print(a,b, b.base is a, b.base)
    print(a,c, c.base is a, c.base)

execute()