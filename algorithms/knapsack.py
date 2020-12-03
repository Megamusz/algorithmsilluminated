def knapsack(items: list, W: int)-> int:
    '''
    Inputs
    1. items, a list containing items, with each item has value/size pair (v, w) 
    2. Capacity W which is the total size avaiable

    Output
    The maximun possible value
    '''
    n = len(items)
    # A = (n + 1) * [(W + 1)*[0]] #Wrong way to define a 2D array in python!
    A = [[0 for x in range(W+1)] for y in range(n+1)] 

    for i in range(1, n+1):
        for x in range(0, W+1):
            vi, wi = items[i-1]
            if wi > x:
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x], A[i-1][x-wi] + vi)

  
    return A[n][W]

def knapsack_optimized(items: list, W: int)-> int:
    n = len(items)
    items = sorted(items, key=lambda item: item[1])
    a = [0 for x in range(W+1)]
    b = [0 for x in range(W+1)]

    for i in range(1, n+1):
        vi, wi = items[i-1]

        b[wi:] = [max(a[x], a[x-wi] + vi) for x in range(wi, W+1)]

        a, b = b, a
        b = a.copy()
  
    return a[W]

def alg(filename):
     with open(filename, 'r') as f:
        W, n = f.readline().strip().split()
        items = []
        for i in range(int(n)):
            v, w = f.readline().strip().split()
            items.append((int(v), int(w)))
        
        return knapsack_optimized(items, int(W))

if __name__ == '__main__':

    with open('tests/problem16.7test.txt', 'r') as f:
        W, n = f.readline().strip().split()
        items = []
        for i in range(int(n)):
            v, w = f.readline().strip().split()
            items.append((int(v), int(w)))
        
        print(knapsack_optimized(items, int(W)))