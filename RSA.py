import mod


def RSA_init():
    nums = mod.find_primes(2)
    n = nums[0]*nums[1]
    phin = (nums[0]-1)*(nums[1]-1)
    e = mod.find_e(phin)
    return (nums, n, phin, e)

data = RSA_init()

def RSA_encrypt(m: int):
    global data
    return pow(m,data[3],data[1])

def RSA_decrypt_naive(c: int):
    global data
    d = mod.mod_inverse(data[3],data[2])
    return pow(c, d, data[1])

def RSA_decrypt_CRT(c: int):
    global data
    d = mod.mod_inverse(data[3],data[2])
    yq = mod.mod_inverse(data[0][0], data[0][1])
    yp = mod.mod_inverse(data[0][1], data[0][0])
    c_p = c%data[0][0]
    c_q = c%data[0][1]

    #Fermat's little theorem
    d_p = d % data[0][0]
    d_q = d % data[0][1]

    #solve system
    m_p = pow(c_p,d_p,data[0][0])
    m_q = pow(c_q,d_q,data[0][1])

    #CRT part
    return (m_p*data[0][0]*yp + m_q*data[0][1]*yq) % data[1]