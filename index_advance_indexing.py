import numpy as np 

def normal_slicing():
    '''
        NORMAL slicing/indexing always returns a VIEW
    '''
    a = np.random.randint(1,19,(5,4))

    print(a[:], a[:].base is a, a[1,2])

def advanced_sliciing():
    '''
        advanced indexing always returns a COPY
    '''
    a = np.array(
        [
             [1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]   

        ]
    )

    row_selector = [0,2]
    column_selector = [0,3]

    #when we apply the row/columns selectpr on the array a, we are performing
    # advanced indexing. is..we select 0th row ,0th col, 2nd row, 3th col

    print(a[row_selector,column_selector],a[row_selector,column_selector].base is None)

    # another way would be to pass ndarrays itself
    print(a[np.array([0,1,2]),np.array([3,1,2])])


    a = np.array(
        [
            [0,1,0],
            [2,1,2],
            [3,2,3],
            [10,4,10]
        ]
    )

    ##how do we select the corners of a 4*3 array
    row_selector = [[0,0],[3,3]]
    column_selector = [[0,2],[0,2]]
    print(a[row_selector,column_selector])

    # since the row selectors and column selectors are basically repeating
    # them selves , we can easily use broadcasting

    row_selector = np.array([0,3])[:, np.newaxis] # columns are repeated so new axis along the columns
    column_selector = np.array([0,2])[np.newaxis, :]
    
    print(row_selector, column_selector, a[row_selector, column_selector])
    
def advanced_sliciing_using_boolean():
    
    a = np.random.randint(1,15, (2,3))

    b = np.full((3), fill_value = True)

    #now if i apply b on a, we will get a falttened 1d tensor as an output, with all selected

    print(a, b)

    c = np.array(

        [
            [True, False, True],
            [False, True, False]
        ]
    ) #will select only 3 since there are only 3 true values.

    print(a[c], a[c].shape)


    a = np.array(
        [
            [1,2,4],
            [4,6,8],
            [1,1,3]
        ]
    )

    print(a[a%2==0]) ##will only return the even numbers


def execute():
    # normal_slicing()
    # advanced_sliciing()
    advanced_sliciing_using_boolean()



execute()
