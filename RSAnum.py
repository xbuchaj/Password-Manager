import random

def nBitRandomNum(n):
    return(random.randrange(2**(n-1)+1, 2**n-1))

def nPrimeNumber(n):
    primeNumbers = []
    if n > 0:
        primeNumbers.append(2)
        i = 3
    while len(primeNumbers) < n:
        flag = True
        for j in range(2, i - 1):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            primeNumbers.append(i)
        i += 1
    return primeNumbers