import numpy as np 

def m_sum():
    
    a = np.array(

        [

            [2,3,4],
            [5,6,7]
        ]
    )

    print(a.sum())#sums every element and returns scalar value
    print(a.sum(axis = 0)) # will sum column wise..hence will return (1,3)
    print(a.sum(axis = 1)) # will sum row wise..hence will return (1,2) [[2+3+4],[5+6+7]]

def min_max():
    a = np.array(

        [

            [2,3,4],
            [5,6,7]
        ]
    )

    print(a.min()) #min of all..returns scalar
    print(a.min(axis=0)) # min column wise [2,3,4]
    print(a.min(axis=1)) # min row wise [2,5]
    
    #argmin returns the index of lowest value row wise or column wise based on axis given
    print(a.argmin()) #min of all..returns scalar
    print(a.argmin(axis=0)) # min column wise [0,0,0] since every 0th column is lowest
    print(a.argmin(axis=1)) # min row wise [0,0]every 0th element in row is lowest


    a = np.array(

        [

            [2,3,4],
            [1,0,7]
        ]
    )

    print(a.argmin()) #min of all..returns scalar
    print(a.argmin(axis=0)) # min column wise [1,1,0] since every 0th column is lowest
    print(a.argmin(axis=1)) # min row wise [0,1] 0th element in 1st row is lowest, 1st element in 2nd row is lowest

    ##similar operations for max, argmax

def mean():
    a = np.array(

        [

            [2,3,4],
            [1,0,7]
        ]
    )

    print(a.mean(axis=0), a.mean(axis=-1), a.mean(axis=1))

    #cumsum takes previous element and keeps summing till all elments are exhausted
    print(a.sum(), a.cumsum(), a.cumsum(axis =0), a.cumsum(axis =1))

def reshaping():
    
    a = np.random.randint(1,10,(4,3))

    print(a.ravel()) ## flattens..but returns a view..so changes are propagated
    print(a.flatten()) ## always returns a copy

    b = a.reshape(-1) #inferred..and flattens..howwever returns a view
    b[0] = 22
    assert b[0] ==a[0,0]

def execute():
    
    # m_sum()
    # min_max()    
    # mean()    
    reshaping()

execute()