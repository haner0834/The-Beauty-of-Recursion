def gcd(n: int, m: int) -> int:
    if n == 0: return m
    return gcd(m%n, n)

def gcd2(n, m):
    while m != 0:
        n, m = m, n % m
    return n
    
print(gcd2(57, 90))