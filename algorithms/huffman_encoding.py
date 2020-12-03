from heap import Heap

def huffman_encoding(A):
    h = Heap()
    l = len(A) * [0]
    for i, a in enumerate(A):
        h.insert((a, (i,)))

    while h.size() > 1:
        a = h.extract()
        b = h.extract()
        key = a[0] + b[0]
        value = a[1] + b[1]
        for i in value:
            l[i] += 1
            
        h.insert((key, value))

    return l

def alg(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        weights = []
        for i in range(n):
            weights.append(int(f.readline().strip()))
        
        l = huffman_encoding(weights)

        max_length = l[0]
        min_length = l[0]
        for v in l:
            max_length = max(max_length, v)
            min_length = min(min_length, v)

        return [max_length, min_length]

if __name__ == '__main__':
    with open('tests/problem14.6test1.txt', 'r') as f:
        n = int(f.readline().strip())
        weights = []
        for i in range(n):
            weights.append(int(f.readline().strip()))
        
        huffman_encoding(weights)
