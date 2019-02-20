import numpy as np 
import time


# theres a sequence of true.false. count the occurence of true to false transition
def count_true_false_transition():

    choices = np.random.choice([True,False], size = 16000000)

    print(choices)

    #one pointer starts right from 0 and another from 1, moving in same direction
    # zips it and den check if False and next is True. if yes, add 1 to list and
    # sums up the list    
    s = time.time()
    print(sum([ 1 for i,j in zip(choices[:], choices[1:]) if not i and  j]))
    print(s-time.time())

    ##numpyionic way : much much faster, pretty apparent when using really large arrays
    s = time.time()
    print(np.count_nonzero(choices[:-1] < choices[1:]))
    ## i cudnt do choices[:] <choices[1:].. since sizes are different
    print(s-time.time())

def sum_two_arrays_element_wise():
    
    a = np.random.randint(1,45, (20))
    b = np.random.randint(1,35, (20))

    print([i+j for i,j in zip(a,b)])
    print(a+b)
    print(np.add(a,b))

def create_2d_array_1onborder_0_inside():

    a = np.ones((6,6)) #2d array..all 1s.
    #we will now populate the interiors with 0s
    # a[1:a.shape[0] - 1, 1: a.shape[1]-1] = 0

    ##better approach..wherver i am doing shape -1 ..can be replaced with -1
    a[1: - 1, 1: -1] = 0
    print(a)

def create_overlapping_chunks():
    '''
        input A = [1,2,3,4,5,6,7,8,9,10]
        output [[1,2,3],[3,4,5],[5,6,7],[7,8,9],[9,10]]
    '''    
    a = list(range(1,11))
    window_size = 3
    b = []
    # hop = 0
    
    # while True:
        
    #     if hop >= len(a):
    #         break

    #     b.append(a[hop: hop + window_size])
    #     hop =hop + window_size -1
    # [hop for hop in range(len(a))]        

    [b.append(a[hop : hop + window_size  ]) for hop in range(0, len(a), window_size -1)]
    
    print(b)

    #much better doesnt require a new list
    print([a[hop : hop + window_size ] for hop in range(0, len(a), window_size -1)])


    # print(np.array_split(a,4)) #doesnt repeat gives 1,2,3 | 4,5,6 ...


def rolling_window():
    '''
    
    given [1,2,3,4,5,6,7,8,9,10]
    o/p [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9],[8,9,10]]

    '''
    a = list(range(1,11))
    window_size = 3
    hop =0
    b = []

    while True:

        if hop+window_size>len(a):
            break
        
        b.append(a[hop: hop+window_size])
        hop+= 1

    print(b)

    print([a[i: i+window_size] for i in range(0, len(a)) if i+window_size <=len(a)])

    from numpy.lib.stride_tricks import as_strided
    a = np.arange(1,11, dtype=np.uint32)

    print(as_strided(a, shape = (a.shape[0] -window_size +1, window_size), strides = (a.strides[-1],a.strides[-1])))


rolling_window()
# create_overlapping_chunks()    
# sum_two_arrays_element_wise()
# create_2d_array_1onborder_0_inside()
# count_true_false_transition()