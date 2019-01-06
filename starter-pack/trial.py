import numpy as np 

#### part one - define tensors #########

#0-D tensor or scalar - a numpy value with 0 dimensions
scalar = np.array(2) ## it cannot be np.array([2]) as this is a 1D vector and 1D tensor
print(scalar.ndim, scalar.shape)
##ndim defines the number of axes


#1D tensor
one_d_tenor = np.array([2])
print(one_d_tenor.ndim, one_d_tenor.shape)

#1D tensor
one_d_tensor = np.array([2,3,4,5,6]) ## this is a 5D vector but a 1D tensor
print(one_d_tensor.ndim, one_d_tenor.shape)

#2D tensors --- array of 1D tensors
two_d_tensor = np.array([
        [1,2,3,4], ## this is the first row
        [11,22,33,44],
        [111,222,333,444]

])

print(two_d_tensor.ndim,  two_d_tensor.shape)


## 3D tensor --- array of 2D tensors

three_d_tensor = np.array([
    [
        [1,2,3],
        [5,6,7]
    ],
    [
        [11,22,33,],
        [55,66,77,]
    ]

])

print(three_d_tensor.ndim, three_d_tensor.shape, three_d_tensor.dtype)

## shape defines how many dimensions a tensor has along each axis
## so in above eg shape = 2,2,3 since they are 2 rows 2 cols..3 items deep
## ndim defines the number of axes.. in above eg it is 3 axes.


#### part one end - define tensors #########




### part two : tensor slicing #######

## you will slice tensors along its axes
## so for 1D you slice only once
## for 2D you may slice twice, separated by a comma

print(one_d_tensor)
print(one_d_tensor[1:3])

print(two_d_tensor)
print(two_d_tensor[1:,:2]) ## essentially take everything frow row1 and till column 2 (0 and 1)

print(two_d_tensor[1:, -2:]) ## in columns, start from 2 columns from the end

print(two_d_tensor[1:, -3: -1]) ## in columns, start from 2 columns from the end, and take  1 columns 

another_two_d = np.random.randint(1,19, (6, 5))
print('another_Two_d:', another_two_d)

print(another_two_d[:, :-2])

print('here:' ,another_two_d[2::2,2::2]) #starts from2nd row.2ndcol and takes every 2 steps in either direction

### part two end: tensor slicing #######

#### part three : broadcasting ######

## we know that operations such as addition are pretty straightforward
## when shapes match of the two tensors. however what happens when the
# shapes of tensors do not match. say t1 = (3, 6) and t2 is (6,)
# what will happen if we try to do t1+t2.
# well in every case, the operations are element wise operations. in this
# case we will try to 'broadcast' the lower dimension of the tensor t2 into
# the same dimension as t1. essentially repeat the 6 elements of t2 3 times
# to create the 2nd axes and perform an element wise operation
# this will be clear in the next example
# caveat would be t1.shape[1] == t2.shape[0] else we will have ambigous broadcasting
# errror

t1 = np.random.randint(1,2, (3,6)) # we create a 3,6 tensor where every element is 1 
t2 = np.random.randint(1,2, (6))

t3 = t1 + t2
assert t1.shape == t3.shape ## lower dimension is broadcast to higher dimension

print(t3) ### expectin all elements to be 2
assert set([2]) == set(t3.flatten().tolist())



#### part three end: broadcasting ######