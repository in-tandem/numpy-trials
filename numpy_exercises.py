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

sum_two_arrays_element_wise()
# create_2d_array_1onborder_0_inside()
# count_true_false_transition()