from floyd_warshall import Graph, floyd_warshall
from bellman_ford import bellman_ford
from dijkstra_shortest_path import dijkstra_shortest_path_heap
import math

def johnson_apsp(G):
    '''
    Johnson's All Pair Shortest Path Algorithm:
    1. From G' by  adding a new vertex s and a new edge (s, v) with length 0 for each v in G
    2. Run Bellman-Ford on G' with source vertex s. [If B-F detects a negative-cost cycle in G' (which must lie in G), halt + report this]
    3. For each v in G, define pv = length of a shortest s-> v path in G'. 
        For each edge e = (u, v) in G, define ce' = ce + pu - pv.
    4. For each vertex u of G: Run Dijkstra's algorithm in G, with edge length {ce'}, with source vertex u, to compute the shortest-path distance d'(u, v) for v in G
    5. For each pair u, v in G, return the shortest-path distance
        d(u, v) := d'(u, v) - pu + pv
    '''
    g_prime = Graph(directed=True)
    n = len(G)
    for v in G:
        for w in G[v]:
            g_prime.add_edge(v, w, G[v][w])
    for v in G:
        g_prime.add_edge(n + 1, v, 0) #let the source vertex to be n+1

    P, _ = bellman_ford(g_prime, n+1)
    if not P: #report negative cycles and halt if the bellman ford detected one
        return None
    for u in G:
        for v in G[u]:
            G[u][v] = G[u][v] + P[u-1] - P[v-1]
    
    A = [[0 for j in range(1+n)] for i in range(1+n)]
    for u in G:
        Dv = dijkstra_shortest_path_heap(G, u)
        for v in G:
            A[u][v] = Dv[v] - P[u-1] + P[v-1]
 
    return A

def alg(filename):
    g = Graph(directed = True)
    g.from_file(filename)

    A = johnson_apsp(g._graph)

    
    negative_cycle = not A
    if negative_cycle:
        return 'NULL'
    n = len(g._graph)   
    min_cost = math.inf  
    if not negative_cycle:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                min_cost = min(min_cost, A[i][j])
        return min_cost

if __name__ == '__main__':

    g = Graph(directed = True)
    g.from_file('tests/problem18.8test1.txt')
    print(johnson_apsp(g._graph))

    
