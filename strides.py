import numpy as np 

def byte_offset():
    '''
        byte offset is the count of bytes starting at 0.
        so if a np array starts with 0, we can get the 
        value at a particular index using offset and strides
    '''
    
    a = np.reshape(np.arange(3*4), (3,4))

    # to get the element of a at 1,2
    offset = sum(np.array([1,2]) * a.strides)

    assert a[1,2] == offset/a.itemsize

    
    a = np.reshape(np.arange(3*4*7), (3,4,7))

    # to get the element of a at 2,3,4
    offset = sum(np.array([2,3,4]) * a.strides)

    assert a[2,3,4] == offset/a.itemsize



    a = np.random.randint(1,4,(2,3))
    offset = sum (a[1,2] * a.strides)
    assert a[1,2]!= offset/a.itemsize ## this is bcoz array doesnt start with 0



def find_stride():
    '''

    numpy arrays are stored as contigous blocks of memory for 1d or any d.
    so stride defines how many bytes we have to move to get to the next block
    of memory in all axis.

    say a = np.random.randint(1,4,(4,)).astype(np.int16)

    np.int16 takes 2 bytes of memory. 
    a is a 1D array. so in order to move to the next item it will take 2*1 stride


    say a = np.random.randint(1,4,(4,3)).astype(np.int32)

    np.int16 takes 4 bytes of memory. 
    a is a 2D array. so in order to move to the next item along the column
    it will take 4*1 stride. however to move to the next item along the row
    it will take 4*a.shape[1] bytes.

    ?how do we get the byte size of an array -- a.itemsize

    so stride = a.itemsize*a.shape[1], a.itemsize

    
    '''
    a = np.random.randint(1,5,(2,3))
    print(a.strides) ## expecting (4*3,4)

    a = np.random.randint(1,3,(4,))
    print(a.strides) ## expecting (4,)

def execute():

    a = np.random.randint(1,5, (2,3))
    print(a.dtype, a.itemsize) ## based on the dtype of the np array, will give the size of bytes
    
    a = a.astype(np.float32)
    print(a.dtype, a.itemsize) ## based on the dtype of the np array, will give the size of bytes
    
    a = a.astype(np.int16)
    print(a.dtype, a.itemsize) ## based on the dtype of the np array, will give the size of bytes

    a = a.astype(np.float64)
    print(a.dtype, a.itemsize) ## based on the dtype of the np array, will give the size of bytes

    find_stride()
    byte_offset()

execute()