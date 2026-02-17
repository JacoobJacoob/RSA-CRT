import random
min_range = pow(2, 100)
max_range = pow(2, 101) - 1
#Uses naive algorithm to check if num is prime
def possible_prime(num: int, bound: int) -> bool:
    for i in range(2,bound):
        if(i%2 == 0): 
            continue
        if num % i == 0:
            return False
    return True

def miller_rabin(num: int, iterations: int) -> int:
    

    return 0
def find_primes(amount: int) -> list[int]:
    global min_range,max_range
    found = 0
    res = []
    candidate = random.randint(min_range,max_range)
    if(candidate % 2 == 0):
        candidate += 1
    while found != amount:
        print(candidate)
        if possible_prime(candidate, 10000):
            print("found!!")
            res.append(candidate)
            found += 1
        candidate += 2
    return res 

#calculate extended GCD and also x,y with euclids alg such that ax+by=gcd(a,b)
def extended_gcd(a: int,b: int) -> tuple:
    if b == 0:
        return a , 0, 1
    gcd, x, y = extended_gcd(b,a%b)
    return (gcd, y - (b//a) * x, x)

def find_e(phin: int) -> int:
    for i in range(2,phin):
        gcd = extended_gcd(phin,i)[0]
        if(gcd == 1):
            return i
    return -1 #illegal output to indicate failure

def mod_inverse(num: int, base: int) -> int:
    gcd, x, y = extended_gcd(num, base)
    if(gcd != 1):
        return -1 #illegal output to indicate failure
    return x%base

print(find_e(24))