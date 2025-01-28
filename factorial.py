def factorial(n: int) -> int:
    if n < 0: return 0
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4))
