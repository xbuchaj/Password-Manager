import random
from RSAnum import RSAnumberGenerator
from configparser import ConfigParser

def keyGenerator():
    p = RSAnumberGenerator()
    q = RSAnumberGenerator()
    n = p * q
    f = (p - 1) * (q - 1)

    def gcd(u, v):
        while v != 0:
            t = v
            v = u % v
            u = t
        return u

    while True:
        b = random.randrange(2, f)
        if gcd(b, f) == 1:
            break
    
    a = ((random.randint(1, 1000) * f) + 1) / b

    configObject = ConfigParser()

    configObject.read("config.ini")
    key = configObject["KEY"]

    key["public"] = str(b)
    key["private"] = str(a)
    key["common"] = str(n)

    with open('config.ini', 'w') as config:
        configObject.write(config)