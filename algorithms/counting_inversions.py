def count_inversions_sort_and_count(A: list):
    n = len(A)
    if n == 1:
        return (A, 0)
    else:
        (B, X) = count_inversions_sort_and_count(A[:n//2])
        (C, Y) = count_inversions_sort_and_count(A[n//2:])
        (D, Z) = count_split_inv(B, C)

        return (D, X + Y + Z)

def count_split_inv(B: list, C: list) -> (list, int):
    nb, nc = len(B), len(C)
    D = []
    i, j = 0, 0
    inv_count = 0
    for k in range(nb + nc):
        if(i >= nb or j >= nc): #any of the two arrays reached the end
            break

        if B[i] < C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
            inv_count += (len(B) - i)

    while i < nb:
        D.append(B[i]) 
        i += 1

    while j < nc:
        D.append(C[j])
        j += 1  
        
    return (D, inv_count)

def count_inversions_brute_force(A: list) -> int:
    i, j = 0, 0
    n = len(A)
    inv_count = 0
    for i in range(n):
        for j in range(i, n):
            if A[j] < A[i]:
                inv_count += 1

    return inv_count

if __name__ == '__main__':
    (X, inv_count) = count_inversions_sort_and_count([ 8,7,6,5,4,3,2,1 ])
  
    
    
    (X, inv_count) = count_inversions_sort_and_count(l)
    print(inv_count)

    # print(count_inversions_brute_force(l))