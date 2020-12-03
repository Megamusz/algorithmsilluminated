def two_sum(A, T):
    d = {}
    for x in A:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    
    sum = 0 # total number of t that distinct x/y in A and satisfy x + y = t
    for t in T:
        found = False
        for x in A:
            y = t - x
            if y in d:
                found = True
                # if y != x or d[x] > 1:
                #     found = True
                #     break

        if found:
            sum += 1
    return sum


def alg(filename):
    with open(filename, 'r') as f:
        A = []
        for line in f.readlines():
            A.append(int(line))
        
        return two_sum(A, range(-10000, 10001))

if __name__ == '__main__':
    with open('tests/problem12.4test.txt', 'r') as f:
        A = []
        for line in f.readlines():
            A.append(int(line))
        
        print(two_sum(A, range(3, 11)))