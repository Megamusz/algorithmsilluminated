

def karasuba_multiplication(x: int, y: int)-> int:
    assert(x >=0 and y >= 0) #for simplicity assuming non-negative integers
    # x = 10^(n/2) * a + b
    # y = 10^(n/2) * c + d
    # then x*y = 10^(n)ac + 10^(n/2)(ad+bc) + bd
    # Gauss's Trick ad + bc = (a+b)*(c+d) - ac - bd
    n = min(len(str(x)), len(str(y)))
    
    if n == 1:
        return x * y
    else:
        p1 = pow(10, n//2)
        p2 = pow(10, 2 * (n//2))
        
        a, b = x // p1, x % p1
        c, d = y // p1, y % p1

        n1 = karasuba_multiplication(a, c)
        n2 = karasuba_multiplication(b, d)
        n3 = karasuba_multiplication(a + b, c + d) - n1 - n2

        return n1*p2 + n3*p1 + n2

