import random
import mod
import time

#Initialises paramaters for RSA
def RSA_init():
    nums = mod.find_primes(2) #[p,q]
    n = nums[0]*nums[1]
    phin = (nums[0]-1)*(nums[1]-1)
    e = mod.find_e(phin) #small number coprime to phin
    return (nums, n, phin, e)

#Input: m, [n,e] -> RSA public key
#Output: encrypted message
def RSA_encrypt(m: int, n: int, e: int):
    return pow(m,e,n)


#Input: c -> encrypted message, [n,e] -> RSA public key , phin -> RSA private key
#Output: decrypted message
#Uses naive approach by just raising to high power mod n
def RSA_decrypt_naive(c: int, n: int, e: int, phin: int):
    d = mod.mod_inverse(e,phin)
    return pow(c, d, n)

#Input: c -> encrypted message, [n,e] -> RSA public key , [phin,[p,q]] -> RSA private key
#Output: decrypted message
#Uses Chinese Remainder Theorem to split the naive equation to smaller parts
def RSA_decrypt_CRT(c: int, e: int, n: int, phin: int, nums: list[int]):
    d = mod.mod_inverse(e,phin)
    y_p = mod.mod_inverse(nums[1], nums[0])
    y_q = mod.mod_inverse(nums[0], nums[1])

    #Fermat's little theorem
    d_p = d % (nums[0] - 1)
    d_q = d % (nums[1] - 1)

    #solve each equation
    m_p = pow(c,d_p,nums[0]) #m_p === c^d_p mod p
    m_q = pow(c,d_q,nums[1]) #m_q === c^d_q mod q

    #CRT part
    #return M1*m_p*y_p      + M2*m_q*y_q     % n
    return (nums[1]*m_p*y_p + nums[0]*m_q*y_q) % n

def main():
    print("beginning RSA...")
    data = RSA_init()
    private_key = [data[0], data[2]]
    public_key = [data[1],data[3]]
    print("primes:\n", private_key[0][0]%10000, private_key[0][1]%10000)
    message = 151515
    print("encrypting: ", message)
    encrypted = RSA_encrypt(message, public_key[0], public_key[1])
    print("encrypted message: ", encrypted)

    start_time = time.perf_counter()

    print("decryption with naive RSA..")
    print("Decrypted: ", RSA_decrypt_naive(encrypted, public_key[0], public_key[1], private_key[1]))
    end_time = time.perf_counter()
    print("total time: ", end_time-start_time)

    start_time = time.perf_counter()

    print("decryption with CRT RSA..")
    print(RSA_decrypt_CRT(encrypted, public_key[1], public_key[0], private_key[1], private_key[0]))
    end_time = time.perf_counter()
    print("total time: ", end_time-start_time)

if __name__ == "__main__":
    main()
