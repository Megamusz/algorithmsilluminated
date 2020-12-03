
def independent_set(weights):
    A = (1 + len(weights)) * [0]
    A[0] = 0
    A[1] = weights[0]

    for i in range(2, len(A)):
        A[i] = max(A[i-1], A[i-2] + weights[i-1])

    i = len(weights)
    S = []
    while i >= 1:
        if A[i-1] >= A[i-2] + weights[i-1]:
            i -= 1
        else:
            S.append(i)
            i -= 2

    return S

def alg(filename):
    pos = [1, 2, 3, 4, 17, 117, 517, 997]
    with open(filename, 'r') as f:
        n = int(f.readline())
        l = []
        for i in range(n):
            l.append(int(f.readline()))
        S = independent_set(l)
        ret = ''
        for p in pos:
            if p in S:
                ret = ret + '1'
            else: 
                ret = ret + '0'

        return ret
        
if __name__ == '__main__':
    with open('tests/problem16.6test.txt', 'r') as f:
        n = int(f.readline())
        l = []
        for i in range(n):
            l.append(int(f.readline()))
        print(independent_set(l))
    