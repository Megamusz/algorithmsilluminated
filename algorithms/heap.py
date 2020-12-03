import operator

class Heap():
    '''
    Simple implementation of Heap structure. could be min/max heap, depending on the initialization
    supported operations:
    1. insert O(logn)
    2. delete_by_index O(logn)
    3. delete O(logn) #note this has to be done through extra book keeping. otherwise it's O(n) in general
    4. extra O(logn)
    '''
    def __init__(self, cmp = operator.lt):
        self.data = []
        # Mapping the value to the index in self.data. this is to avoid searching (which needs O(n) time) during deletion.
        # To maintain this mapping, extra work has to be done every when swap happens
        self.imap = {} 
        self.cmp = cmp

    def _swap(self, i, j):
        d = self.data
        im = self.imap

        im[d[i][1]], im[d[j][1]] = im[d[j][1]], im[d[i][1]] 
        d[i], d[j] = d[j], d[i]
        

    def insert(self, entry):
        d = self.data
        if len(entry) == 1:
            entry = (entry[0], entry[0])
        d.append(entry)
        
        self.imap[entry[1]] = len(d) - 1
        self._bubble_up(len(d) - 1)

    def delete_by_index(self, i):
        '''
        O(logn) to delete the specified element (index)
        '''
        d = self.data
        im = self.imap


        self._swap(-1, i)

        del im[d[-1][1]]
        ret = d.pop()
        

        if i < len(d):
            self._bubble_down(i)
            self._bubble_up(i)
        return ret[0]

    def delete(self, value):
        '''
        O(1) to find the element index by value and O(logn) delete it 
        '''
        if value in self.imap:
            i = self.imap[value]
            return self.delete_by_index(i)
        

    def _bubble_up(self, i):
        d = self.data
        im = self.imap
        while i:
            pi = (i - 1)//2 
            if not self.cmp(d[pi][0], d[i][0]):
                self._swap(pi, i)
                i = pi 
            else: #heap property already holds, exit
                break

    def _bubble_down(self, i):
        d = self.data
        im = self.imap
        n = len(d)

        while i < n:
            c1 = 2*i + 1
            c2 = 2*i + 2
            if c2 < n: #both children exist, pick the index from the smaller(bigger) child
                j = c1 if self.cmp(d[c1][0], d[c2][0]) else c2
            elif c1 < n:#only left child, pick it's index
                j = c1
            else: 
                break #already reached the last level, exit

            if self.cmp(d[j], d[i]):
                self._swap(j, i)
                i = j
            else:
                break

    def extract(self): 
        ''' extra the first element (min/max)
        '''
        im = self.imap
        d = self.data

        if len(d) == 0:
            return None
        else:
            
            self._swap(0, -1) #swap the min element to the last position and pop out
            del im[d[-1][1]]
            ret = d.pop()
            
            self._bubble_down(0)

            return ret

    def top(self):
        return self.data[0]

    def size(self):
        return len(self.data)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, list(self.data))


if __name__ == '__main__':
    h = Heap()

    h.insert((4, 'a'))
    h.insert((3, 'b'))
    h.insert((2, 'c'))
    h.insert((1, 'd'))
    print(h)

    h.delete('c')
    print(h)

    print(h.extract())
    print(h)


    h2 = Heap(operator.gt)
    h2.insert((1, 'a'))
    h2.insert((2, 'b'))
    h2.insert((3, 'c'))
    h2.insert((4, 'd'))
    print(h2)
    print(h2.extract())
    print(h2)
            