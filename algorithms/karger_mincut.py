from union_find import UnionFind
import random
import math

# import networkx as nx
# import matplotlib.pyplot as plt

def karger_mincut(G, n):
    '''
    Inputs
    G is represented by a list of edges (undirected), n is the number of vertices

    Output
    Two partitions represented by found min cut
    '''
    N = n**2*math.log(n)

    min_edges = len(G)
    
    for t in range(N):
        G_ = G.copy()
        random.seed()
        
        uf = UnionFind()
        for v in range(1, n+1):
            uf.insert(v)

        random.shuffle(G_)

        while len(uf.group) > 2:
            u, v = G_.pop()
            uf.union(u, v)

        A, B = uf.group.values()
        count = 0
        for u, v in G:
            if (u in A and v in B) or (v in A and u in B): #edge that crossing the cut
                count +=1 
        if min_edges > count:
            cut = (A, B)
            min_edges = count
    return cut

if __name__ == '__main__':
    
    G = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
    for i in range(10):
        print(karger_mincut(G, 4))

    # g = nx.Graph(G)
    # nx.draw_networkx(g)
    # plt.show()