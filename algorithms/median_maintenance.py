from heap import Heap
import operator

def median_maintenance(l):
    h_lo = Heap(operator.gt)
    h_hi = Heap(operator.lt)
    sum = 0 #sum of the medians
    k = 0
    for i in l:
        k += 1

        if h_lo.size() == 0:
            h_lo.insert((i,))
            m = i
        else:
            if i < h_lo.top()[0]: 
                h_lo.insert((i,))
                if h_lo.size() > k/2:
                    h_hi.insert(h_lo.extract())
            else:
                h_hi.insert((i,))
                if h_hi.size() > k/2:
                    h_lo.insert(h_hi.extract())
        
            if h_lo.size() == (k + 1) // 2:
                m = h_lo.top()[0]
            else:
                m = h_hi.top()[0]
           
        sum += m
    return sum % 10000

def alg(filename):
     with open(filename, 'r') as f:
        l = f.readlines()
        l = [int(i) for i in l]
        return median_maintenance(l)

if __name__ == '__main__':
    with open('tests/problem11.3test.txt', 'r') as f:
        l = f.readlines()
        l = [int(i) for i in l]
        print(median_maintenance(l))
