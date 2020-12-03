import math

def optimal_bst(W):
    n = len(W)
    A = [[0 for j in range(len(W))] for i in range(len(W))]

    for s in range(n): #j-i
        for i in range(n):
            if i + s > n-1:
                continue
            min_cost = math.inf
            for r in range(i, i+s+1):
                c = sum(W[i:i+s+1])
                if r > i:
                    c += A[i][r-1]
                if r < i+s and r < n-1:
                    c += A[r+1][i+s]
                min_cost = min(min_cost, c)
            
            A[i][i+s] = min_cost
    
    return A[0][n-1]

if __name__ == '__main__':
    with open('tests/problem17.8optbst.txt', 'r') as f:
        n = int(f.readline().strip())
        W = [int(x) for x in f.readline().strip().split(',')]
        assert(len(W) == n)
        print(optimal_bst(W))