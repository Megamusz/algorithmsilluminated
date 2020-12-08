
def merge_sort(A):

    n = len(A)

    if n <= 1:
        return A
    
    Al = merge_sort(A[:n//2])
    Ar = merge_sort(A[n//2:])

    Am = []
    i, j = 0, 0
    for k in range(n):
        if i > len(Al) - 1 or j > len(Ar) - 1:
            break
        if Al[i] < Ar[j]:
            Am.append(Al[i])
            i+=1
        else:
            Am.append(Ar[j])
            j+=1

    while i < len(Al):
        Am.append(Al[i])
        i+=1
    while j < len(Ar):
        Am.append(Ar[j])
        j+=1

    return Am

if __name__ == '__main__':
    print(merge_sort([7, 8, 9, 6, 5, 4, 3, 2, 1]))
    print(merge_sort([1]))
    print(merge_sort([2, 1]))
    print(merge_sort([1, 2, 3, 4]))