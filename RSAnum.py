import random

def nBitRandomNum(n):
    return(random.randrange(2**(n-1)+1, 2**n-1))