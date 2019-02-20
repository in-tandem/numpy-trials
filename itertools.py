import itertools as it 
from itertools import zip_longest, accumulate
### example of using zip longest vs zipp
## usual zip stops at the smallest list
## to circumvent that and keep going while adding none to missing values.
l2 = [1,2,3,4,5,6,7]
l1 = ['A','B','C']

# this will stop at (3,C)
print([i for i in zip(l2,l1)])

# this will stop at (7,None)
print([i for i in zip_longest(l2,l1)])


## take a subsample of k length in varying forms from a sample of n
## they only take in ascending lexicogrpahic way.. and no repeats
print(list(it.combinations(range(1,4),2)))

## if you want repeats
print(list(it.combinations_with_replacement(range(1,4),2)))


##selection n permutations of an iterable 
print(list(it.permutations(range(1,4),3)))
print(list(it.permutations(['a','b','c'],3)))


##create an infinite sequence 
infinite_even_numbers = it.count(0,2) #start from 0, take every second step
print([next(infinite_even_numbers) for i in  range(10)])
print(list(zip(infinite_even_numbers, ['a','b','c'])))


def intermediate(p,s):
    return p*s

def recurrence(p, s, constant, function):
    # t1= function(p,s)
    t2 = function(p,s) + constant
    
    while True:
        yield t2
        # s= t2
        t2 = function(p,t2) + constant


t1= recurrence(1,0,2,intermediate)
print(t1, recurrence(1,t1,2,intermediate))

# for i in recurrence(1,0,2,intermediate):
    
#     if i <10:
#         print(i)
#     else:
#         break

print(list(accumulate([0,1,2,3,4], lambda x,y : x+y)))