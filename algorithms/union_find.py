
class UnionFind(object):
    def __init__(self):
        self.leader = {} # record the leader for each object {x: x, y: x, z: x}
        self.group = {} #record the items under each group, index by leader {x: {x, y, z}}

    def insert(self, x):
        assert(x not in self.leader)
        self.leader[x] = x
        self.group[x] = set()
        self.group[x].add(x) 

    def find(self, x):
        if x in self.leader:
            return self.leader[x]
        else:
            return None

    def size(self, x):
        leader = self.find(x)
        if leader:
            return len(self.group[leader])
        else:
            return 0

    def union(self, x, y):
        a, size_a = self.find(x), self.size(x)
        b, size_b = self.find(y), self.size(y)

        if a == b or size_a == 0 or size_b == 0:
            return 

        if size_a < size_b:
            #modify leaders in group in a to b
            for i in self.group[a]:
                self.leader[i] = b
                self.group[b].add(i)
            del self.group[a]
        else:
            #modify leaders in group in a to b
            for i in self.group[b]:
                self.leader[i] = a
                self.group[a].add(i)
            del self.group[b]

    def __str__(self):
        return '{}(leader: {}, group: {})'.format(self.__class__.__name__, self.leader, self.group)

if __name__ == '__main__':
    uf = UnionFind()

    uf.insert(1)
    uf.insert(2)
    uf.insert(3)
    uf.insert('a')
    uf.insert('b')
    uf.insert('c')

    print(uf)
    uf.union(1, 3)
    print(uf)
    uf.union(1, 2)
    print(uf)
    uf.union('a','b')
    print(uf)