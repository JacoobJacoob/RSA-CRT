import random
min_range = pow(2, 1024)
max_range = pow(2, 1025) - 1
#Uses naive algorithm to check if num is prime
def possible_prime(num: int, bound: int) -> bool:
    for i in range(2,bound):
        if(i%2 == 0): 
            continue
        if num % i == 0:
            return False
    return True

#Uses miller-rabin primality test; page 156 rosen; to test if num is prime in a random base a for some iterations
#after the iterations, has 0.25^iterations chance to be composite
def miller_rabin(num: int, iterations: int) -> bool:
    temp = num - 1
    #find s,t such that num - 1 = d*(2^s)
    s = 0
    while(temp%2 == 0):
        temp //= 2
        s += 1
    d = temp

    #check iterations times if num passes miller's test for base a
    for i in range(0, iterations):
        a = random.randint(2,num-2)
        x = pow(a,d,num)
        for j in range(0,s):
            x = pow(x,2,num)
        if x != 1:
            return False
    return True

#Returns a list[amount] with higly likely primes
def find_primes(amount: int) -> list[int]:
    global min_range,max_range
    res = []
    while amount != 0:
        #get random odd int in range
        candidate = random.randint(min_range,max_range)
        if(candidate % 2 == 0):
            candidate += 1
        if possible_prime(candidate, 10000):
            if miller_rabin(candidate, 100):#so (0.25)^100 chance to not be prime
                res.append(candidate)
                amount -= 1
    return res 

#calculate extended GCD and also x,y with euclids alg such that ax+by=gcd(a,b) recuresivly
def extended_gcd(a: int,b: int) -> tuple[int,int,int]:
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_gcd(b,a%b)
    return (gcd, y, x - (a//b)*y)

def find_e(phin: int) -> int:
    for i in range(2,phin):
        gcd = extended_gcd(phin,i)[0]
        if(gcd == 1):
            return i
    return -1 #illegal output to indicate failure

def mod_inverse(num: int, base: int) -> int:
    gcd, x, y = extended_gcd(num, base)
    if(gcd != 1):
        print("!!!!!!")
        return -1 #illegal output to indicate failure
    return x%base

print(find_e(24))