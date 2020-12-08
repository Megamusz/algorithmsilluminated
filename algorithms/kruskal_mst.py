from union_find import UnionFind

def kruskal_mst(G, n):
    '''
    Input:
    Graph G is reprented by a list of edges, e.g. [((1, 2), 5), ((2, 3), 6)], this means the graph has two edges (1, 2) and (2, 3), with weight 5 and 6 respectively
    n is the number of vertices in the graph. assuming the vertices are indexed by 1 ... n

    Output:
    The minimun spanning tree T with selected edges from G. 
    To get the cost, just loop over all the edges and sum over the weights

    Kruskal's MST algorithm
    - Sort edges in order of increasing cost O(mlogn)
    - T = {}
    - For i = 1 to m
        - If T U {i} has no cycles
            - Add i to T
    - Return T
    '''
    sorted_edges = sorted(G, key=lambda x: x[1])
    m = len(sorted_edges)
    T = set()

    uf = UnionFind()
    for v in range(1, n+1):
        uf.insert(v)

    for i in range(m):
        (u, v), w = sorted_edges[i]
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            T.add(sorted_edges[i])

    return T


if __name__ == '__main__':
    
    with open('tests/problem15.9.txt', 'r') as f:
        n, m = f.readline().strip().split()
        G = []
        for _ in range(int(m)):
            u, v, w = f.readline().strip().split()
            G.append(((int(u), int(v)), int(w)))
        print(kruskal_mst(G, int(n)))