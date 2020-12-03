
from random import randint

def quick_sort(A: list, l: int, r: int):
    '''
    in-place quick sort algorithm 
    @param A: to be sorted array
    @param l: left index of the A, inclusive
    @param r: right index of the A, exclusive
    '''
    n = r - l
    if n <= 1:
        return 

    p = partition(A, l, r)
    #Recursively sort 1st part
    quick_sort(A, l, p)
    #Recursively sort 2nd part
    quick_sort(A, p+1, r)


def partition(A: list, l: int, r: int) -> int:
    '''
    partition around the piviot, return the index of the pivot in the array
    '''
    #first element as pivot
    p = l 

    # random pivot
    # p = randint(l, r-1)
    # A[p], A[l] = A[l], A[p] #move pivot to the first position
    # p = l

    i, j = l + 1, l + 1
    for j in range(l+1, r):
        if A[j] < A[p]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i-1], A[p] = A[p], A[i-1]

    return i-1

if __name__ == '__main__':
    A = [4, 3,2,1]
 
    quick_sort(A, 0, len(A))

    print(A)