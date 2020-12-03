from collections import defaultdict
import dijkstra_shortest_path
import math

def floyd_warshall(G):
    n = len(G)

    A = [[[0 for j in range(n+1)] for i in range(n+1)] for k in range(n+1)]
    #initialize A:
    # if i == j then A[i][j][0] = 0
    # else there's edge from i -> j, then A[i][j][0] = edge cost of i->j
    # else A[i][j][0] = infinity
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                if j in G[i]: #in case self loop has negative cycle
                    A[0][i][j] = min(G[i][j], 0)
                else:
                    A[0][i][j] = 0 
            elif j in G[i]:
                A[0][i][j] = G[i][j]
            else:
                A[0][i][j] = math.inf

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                A[k][i][j] = min(A[k-1][i][j], A[k-1][i][k] + A[k-1][k][j])
        
    return A[n]

class Graph(dijkstra_shortest_path.Graph):

    def from_file(self, filename):
        with open(filename, 'r') as f:
            n, m = f.readline().strip().split()
            for _ in range(int(m)):
                s, t, w = f.readline().strip().split()
                self.add_edge(int(s), int(t), int(w))

            #Note: this is assuming we have all the vertexes from 1...max_node
            # In case any of the node not presenting in the text file, it is a separate node disconnect to the graph
            # that's why we need the following postprocessing pass to add those missing separated vertexes
            for i in range(1, int(n) + 1):
                if i not in self._graph:
                    self.add_vertex(i)

def alg(filename):
    g = Graph(directed = True)
    g.from_file(filename)

    A = floyd_warshall(g._graph)
    min_cost = math.inf

    n = len(g._graph)
    negative_cycle = False
    for i in range(1, n + 1):
        if A[i][i] < 0:
            negative_cycle = True
            return 'NULL'
            
    if not negative_cycle:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                min_cost = min(min_cost, A[i][j])
        return min_cost

if __name__ == '__main__':


    g = Graph(directed = True)
    g.from_file('tests/input_random_6_4.txt')
    n = len(g._graph)
    print(g)

    A = floyd_warshall(g._graph)
    min_cost = math.inf

    negative_cycle = False
    for i in range(1, n + 1):
        if A[i][i] < 0:
            negative_cycle = True
            print('Negative cycle detected')
            break

    if not negative_cycle:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                min_cost = min(min_cost, A[i][j])
        print(min_cost)
    