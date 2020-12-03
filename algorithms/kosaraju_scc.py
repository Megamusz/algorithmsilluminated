from graph import Graph
from queue import LifoQueue

# import networkx as nx
# import matplotlib.pyplot as plt

class Stack():
    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def put(self, v):
        self.data.append(v)

    def empty(self):
        return len(self.data) == 0

def reverse(graph):
    '''
    Return the reversed graph. O(m + n)
    '''
    g_rev = Graph()
    for v, ws in graph.items():
        if len(ws) == 0:
            g_rev.add_vertex(v)
        else:
            for w in ws:
                g_rev.add_edge(w, v)

    return g_rev._graph

def kosaraju_scc(graph):
    ''' Kosaraju's Two-Pass Algorithm
    Complexity: O(m + n)
    1. Let Grev = G with all arcs reversed
    2. Run DFS-Loop on Grev
        Let f(v) = "finishing time" of each v in V
    3. Run DFS-Loop on G
        processing nodes in decreasing order of finishing times

    Note: Assuming graph is represented by dict of set, e.g. {'a': {'b', 'c'}, 'b': {'c'}}
    '''
    def DFS_1pass(graph, i):
        visited.add(i)
        stack = Stack()
        stack.put(i)

        while not stack.empty():
            #pop the vertex only when it's done, i.e. all of it's children are visited
            # this is to calculate the
            v = stack.top() 

            done = True
            for w in graph[v]:
                if w not in visited:
                    visited.add(w)
                    stack.put(w)
                    done = False
            
            if done: 
                stack.pop()      
                nonlocal t
                l[t] = v
                t += 1
                f[v] = t
        

    def DFS_2pass(graph, i):
        counter = 0
        
        visited.add(i)
        leader[i] = s

        stack = LifoQueue()
        stack.put(i)

        while not stack.empty():
            v = stack.get()
            counter += 1
            
            for w in graph[v]:
                if w not in visited:
                    visited.add(w)
                    stack.put(w)
        
        return counter

    leader = {}
    s = None
    t = 0
    f = {} #finishing time for each vertex
    g = graph
    grev = reverse(graph)
    n = len(graph)
    l = n * [0] #ordered vertext list for the 2nd pass scan

    visited = set()
    for i in grev:
        if i not in visited:
            DFS_1pass(grev, i)

    visited.clear()
    scc_counters = []

    for i in reversed(l):
        if i not in visited:
            s = i
            counter = DFS_2pass(g, i)
            scc_counters.append(counter)
    while len(scc_counters) < 5:
        scc_counters.append(0)

    scc_counters.sort(reverse=True)
    return scc_counters[0:5]

def alg(file):
    g = Graph(directed = True)
    g.from_file(file)

    ret = kosaraju_scc(g._graph)
    return ','.join([str(s) for s in ret])

if __name__ == '__main__':
    
    g = Graph(directed = True)
    g.from_file('tests/input_mostlyCycles_3_8.txt')

    print(kosaraju_scc(g._graph))

    # G = nx.DiGraph(g._graph)

    # nx.draw_networkx(G)
    # plt.show()