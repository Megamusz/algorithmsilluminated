
import math
import random
def papadimitriou_2sat(A, n):
    
    T1 = int(math.log2(n))
    T2 = 2*(n**2)

    for t in range(T1):
        #choose random initial assignment
        x = [random.random() > 0.5 for _ in range(n+1)]
        for i in range(T2):
            unsat = evaluate(A, x)
            if len(unsat) == 0:
                return 1
            else:
                i = random.choice(unsat)
                j = random.choice([0, 1])
                #randomly choose one unsatisfied clauss and flip one of the variable uniformly
                x[abs(A[i][j])] = not x[abs(A[i][j])]

    return 0

def evaluate(A, x):
    unsatisfy_index = []

    for i, (i1, i2) in enumerate(A):
        v1 = not x[-i1] if i1 < 0 else x[i1]
        v2 = not x[-i2] if i2 < 0 else x[i2]
        if not (v1 or v2):
            unsatisfy_index.append(i)
        
    return unsatisfy_index

def alg(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        A = []
        for i in range(n):
            a, b = f.readline().strip().split()
            A.append((int(a), int(b)))
        
        return papadimitriou_2sat(A, n)

if __name__ == '__main__':
    with open('tests/input_beaunus_4_4.txt', 'r') as f:
        n = int(f.readline().strip())
        x = [True for i in range(n+1)]
        A = []
        for i in range(n):
            a, b = f.readline().strip().split()
            A.append((int(a), int(b)))
        
        print(papadimitriou_2sat(A, n))