from random import randint
def rselect(A: list, l: int, r: int, i):
    '''
    randomized selection algorithm 
    @param A: to be sorted array
    @param l: left index of the A, inclusive
    @param r: right index of the A, exclusive
    @param i: order statistic
    '''
    n = r - l
    if n == 1:
        return A[l]

    j = partition(A, l, r)

    if j == i:
        return A[j]
    elif j > i:
        #Recursively find in the 1st part
        return rselect(A, l, j, i)
    else:
        #Recursively find in the 2nd part
        return rselect(A, j+1, r, i)


def partition(A: list, l: int, r: int) -> int:
    '''
    partition around the piviot, return the index of the pivot in the array
    '''
    # p = l #first element as pivot
    p = randint(l, r-1) # random pivot
    A[p], A[l] = A[l], A[p] #move pivot to the first position
    p = l

    i, j = l + 1, l + 1
    for j in range(l+1, r):
        if A[j] < A[p]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i-1], A[p] = A[p], A[i-1]

    return i-1


if __name__ == '__main__':
    A = [ 5, 4, 3, 2, 1]

    print(rselect(A, 0, len(A), 4))

    # with open('tests/problem6.5test1.txt', 'r') as f:
    #     l = [int(l.strip()) for l in f.readlines()]
    #     print(rselect(l, 0, 10, 4))


    