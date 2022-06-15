def factorial(n):
    # f = n (n-1) (n-2) .... 1
    f = 0
    for m in range(n):
        if m == 0:
            f = 1
        f = f * (m + 1)
    return f

def factorialR(n):
    if(n>0):
        return n*factorialR(n-1)
    else:
        return 1

print(factorialR(5))
