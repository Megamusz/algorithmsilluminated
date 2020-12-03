def sequence_alignment(X, Y, penalty_gap, penalty_mismatch):
    m, n = len(Y), len(X)
    A = [[0 for x in range(n+1)] for y in range(m+1)] 

    for i in range(m+1):
        A[i][0] = i*penalty_gap
    
    for j in range(n+1):
        A[0][j] = j*penalty_gap


    for i in range(1, m+1):
        for j in range(1, n+1):
            A[i][j] = min(
                A[i-1][j-1] + (Y[i-1] != X[j-1])*penalty_mismatch, 
                min(A[i-1][j] + penalty_gap, A[i][j-1]+penalty_gap)
                )
    
    return A[m][n]

if __name__ == '__main__':
    with open('tests/problem17.8nw.txt', 'r') as f:
        n, m = f.readline().strip().split()
        penalty_gap, penalty_mismatch = f.readline().strip().split()

        X = f.readline().strip()
        Y = f.readline().strip()

        assert(len(X) == int(n))
        assert(len(Y) == int(m))

        print(sequence_alignment(X, Y, int(penalty_gap), int(penalty_mismatch)))