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

def LowLevelPrimalityTest(candidate, nPrimes):
    PrimeNumbers = nPrimeNumber(nPrimes)
    for i in range(len(PrimeNumbers)):
        if candidate % PrimeNumbers[i] == 0:
            return False
    return True

def MillerRabinTest(candidate, k):
    maxDivisionsByTwo = 0
    ec = candidate-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == candidate-1)
 
    def trialComposite(round_tester):
        if pow(round_tester, ec, candidate) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, candidate) == candidate-1:
                return False
        return True
 
    for i in range(k):
        round_tester = random.randrange(2, candidate)
        if trialComposite(round_tester):
            return False
    return True           