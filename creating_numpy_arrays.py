import numpy as np 

def execute():
    '''

        we look at different ways to create numpy arrays

    '''
    
    # first , manually typing it
    print(np.array([[12,21],[22,31]]))

    # using random.randint for creating int arrays
    print(np.random.randint(2,15,(4,3)))

    #using random.rand for creating float arrays within 0 and 1
    print(np.random.rand(4,3))

    #using random.uniform to create float arrays within a range
    print(np.random.uniform(1,19,(2,3)))

    #create np array of certain shape all containing zeros
    print(np.zeros((3,4))) ## by default is float
    print(np.zeros((1,2)).astype(np.int32)) # cast to int

    #create np arrays containing all ones
    print(np.ones((3,4))) #by default float
    print(np.ones((3,4)).astype(np.int32))
    print(np.random.randint(1,2,(3,4)))

    ##create np arrays containing a certain value
    print(np.full((2,3),fill_value = True))


    #create np arrays by stepping over a range in equal intervals
    print(np.linspace(1,23,num=6)) ##always returns a 1D
    print(np.arange(1,23,step = 5)) ##every fifth step, always returns 1D array
    print(np.arange(1,60,step=10).reshape((3,2)))

    #create empty array
    print(np.empty((3,4))) ## values are randomly initialized to something..to be used
    # when we are going to overwrite the entries anyways or we dont care what the 
    # initial values of the np array are 


    #promoting 1D array to higher order
    a = np.arange(1,10)
    print(a, a.ndim, a.shape)
    aa = a[np.newaxis,:] ## adding a new axis at the start..hence one row
    print(aa, aa.ndim, aa.shape)
    aaa = a[:, np.newaxis] ## adding a new axis at the end... hence one column
    print(aaa,aaa.ndim, aaa.shape)


    ## slicing/indexing creates views and not copies. hence changes made are propagated as well
    a = np.random.randint(1,9,(6))
    aa = a[2:]
    aa[0] = 78
    print(aa)
    assert aa[0] ==a[2] ## changes propagated

    ## similar with transpose /returns views..hence changes are propagated
    a = np.random.randint(2,7,(2,2))
    b = a.T
    b[0,0] = 888
    assert b[0,0] == a[0,0]

    b = np.transpose(a)
    b[0,0] = 888
    assert b[0,0] == a[0,0]

    ##how to create a copy and not a view?
    b = np.array(a.T)
    b[0,0] = 777
    assert b[0,0] != a[0,0]

    ## creating a identity matrix..ie square matrix with diagonals as 1
    print(np.eye(3))

execute()