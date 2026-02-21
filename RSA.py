import random
import mod
import time
import RSA_Objects

#Initialises paramaters for RSA
def RSA_init():
    nums = mod.find_primes(2) #[p,q]
    n = nums[0]*nums[1]
    private = RSA_Objects.privateKey(nums[0],nums[1])
    e = mod.find_e(private.phin) #small number coprime to phin
    public = RSA_Objects.publicKey(n,e)
    return private, public

#Input: m, [n,e] -> RSA public key
#Output: encrypted message
def RSA_encrypt(m: int, public : RSA_Objects.publicKey):
    return pow(m, public.e, public.n)


#Input: c -> encrypted message, [n,e] -> RSA public key , phin -> RSA private key
#Output: decrypted message
#Uses naive approach by just raising to high power mod n
def RSA_decrypt_naive(c: int, public: RSA_Objects.publicKey, private: RSA_Objects.privateKey):
    d = mod.mod_inverse(public.e, private.phin)
    return pow(c, d, public.n)

#Input: c -> encrypted message, [n,e] -> RSA public key , [phin,[p,q]] -> RSA private key
#Output: decrypted message
#Uses Chinese Remainder Theorem to split the naive equation to smaller parts
def RSA_decrypt_CRT(c: int, public: RSA_Objects.publicKey, private: RSA_Objects.privateKey):
    d = mod.mod_inverse(public.e,private.phin)
    y_p = mod.mod_inverse(private.q, private.p)
    y_q = mod.mod_inverse(private.p, private.q)

    #Fermat's little theorem
    d_p = d % (private.p - 1)
    d_q = d % (private.q - 1)

    #solve each equation
    m_p = pow(c,d_p,private.p) #m_p === c^d_p mod p
    m_q = pow(c,d_q,private.q) #m_q === c^d_q mod q

    #CRT part
    #return M1*m_p*y_p      + M2*m_q*y_q     % n
    return (private.q*m_p*y_p + private.p*m_q*y_q) % public.n

def main():
    print("beginning RSA...")
    private_key, public_key = RSA_init()
    print("primes:\n", private_key.p%10000, private_key.q%10000)

    amount = 1000
    bit_length = 512
    total_time_naive = 0
    total_time_CRT = 0
    for i in range(amount):
        message = random.randint(pow(2,bit_length),pow(2,bit_length+1) - 1)
        print("encrypting: ", message)
        encrypted = RSA_encrypt(message, public_key)
        #print("encrypted message: ", encrypted)

        start_time = time.perf_counter()
        RSA_decrypt_naive(encrypted, public_key, private_key)
        #print("Decrypted: ", )
        total_time_naive += time.perf_counter() - start_time

        start_time = time.perf_counter()
        RSA_decrypt_CRT(encrypted, public_key, private_key)
        #print("Decrypted with CRT: ",)
        total_time_CRT += time.perf_counter() - start_time
    print(f"total time with naive approach {total_time_naive} and per {amount} is {total_time_naive/amount}")
    print(f"total time with CRT {total_time_CRT} and per {amount} is {total_time_CRT/amount}")

if __name__ == "__main__":
    main()
