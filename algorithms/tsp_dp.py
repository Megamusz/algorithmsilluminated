 
from itertools import combinations
from collections import defaultdict
import math
import floyd_warshall

def tsp_dp(G):
    n = len(G)
    V = [i+2 for i in range(n-1)]
    A = defaultdict(dict)
    for m in range(0, n):
        for S_1 in combinations(V, m): #Subset w/o vertex 1
            S = (1, *S_1)
            if S == (1, ):
                A[S][1] = 0
            else:
                A[S][1] = math.inf
                
    for m in range(1, n):
        for S_1 in combinations(V, m): #Subset w/o vertex 1
            S = (1, *S_1)
            for j in S_1:
                S_j = tuple([x for x in S if x != j])
                A[S][j] = math.inf
                for k in S_j:
                    A[S][j] = min(A[S][j], A[S_j][k] + G[k][j])
    
    min_cost = A[(1, *V)][2] + G[2][1]
    for j in range(3, n):
        min_cost = min(min_cost, A[(1, *V)][j] + G[j][1])

    return min_cost

class Graph(floyd_warshall.Graph):
    def from_file2(self, filename):
        #READ the file with format #2: each vertex is a point in the plane, 
        #the cost between vertices are the Eulidean distance between its endpoints
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            points = []
            for _ in range(int(n)):
                x, y = f.readline().strip().split()
                points.append((float(x), float(y)))
            for i in range(n):
                for j in range(i + 1, n):
                    xi, yi = points[i]
                    xj, yj = points[j]
                    d = ((xi-xj)*(xi-xj) + (yi-yj)*(yi-yj))**0.5
                    self.add_edge(i+1, j+1, d)

def alg(filename):
    g = Graph(directed=False)
    g.from_file2(filename)
    return math.floor(tsp_dp(g._graph))

if __name__ == '__main__':
    
    g = Graph(directed=False)
    g.from_file('tests/tsptest2.txt')
    print(tsp_dp(g._graph))

    g2 = Graph(directed=False)
    g2.from_file2('tests/tsptest3.txt')
    print(round(tsp_dp(g2._graph), 2))

    # g3 = Graph(directed=False)
    # g3.from_file2('tests/tspfile1.txt')
    # print(tsp_dp(g3._graph))