import math

# simple factoring
def factoring_simple(n):
    factors = []
    i = 2 
    # start factoring
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    # case) n * 1
    if n > 1:
        factors.append(n)
    return print(factors)

# fermat prime factoring
def factoring_fermat(n):
    x = math.ceil(math.sqrt(n))
    y2 = x*x - n
    # Validate that y is an integer
    while not math.sqrt(y2).is_integer():
        x += 1
        y2 = x*x - n
    
    # Create prime factor
    p = x + math.isqrt(y2)
    q = x - math.isqrt(y2)
    return print(p, q)

factoring_simple(11)
factoring_simple(100)
factoring_simple(12345)
factoring_simple(1000001)
factoring_simple(2**16)

print('----------')

factoring_fermat(15)
factoring_fermat(119)
factoring_fermat(187)
factoring_fermat(2987)
factoring_fermat(6750311)