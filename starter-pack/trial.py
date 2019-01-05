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
print(another_two_d)

print(another_two_d[:, :-2])

### part two end: tensor slicing #######