import math

flt_zeta = []

def fill_zeta_outcome():
    
    flt_zeta.append(-1)                     # Zeta (1) not defined
    flt_zeta.append(math.pi ** 2 / 6)       # Zeta(2)
    flt_zeta.append(1.2020569031595942853)  # Zeta(3)
    flt_zeta.append(math.pi ** 4 / 90)
    flt_zeta.append(1.0369277551433699263)
    flt_zeta.append(math.pi ** 6 / 945)
    flt_zeta.append(1.0083492773819228268)
    flt_zeta.append(math.pi ** 8 / 9450)
    flt_zeta.append(1.0020083928260822144)
    flt_zeta.append(math.pi ** 10 / 93555)
    flt_zeta.append(1.0004941886041194645)
    flt_zeta.append(691 * math.pi ** 12 / 638512875 )   
    flt_zeta.append(1.0001227133475784891)
    flt_zeta.append((2 * (math.pi ** 14)) / 18243225)
    flt_zeta.append(1.0000305882363070204)

    print(flt_zeta, sep = "\n")
    
def pi_Leibnitz():

    int_outcome = 1
    int_sign = -1
    for i in range(3,2000, 2):
        int_outcome = int_outcome + (int_sign * 1/i)
        if int_sign == 1:
            int_sign = -1
        else:
            int_sign = 1
    print(f'{int_outcome:.25f}')
    print(f'{math.pi:.25f}')
    print(f'{math.pi/4:.25f}')
    print("Verschil: " , int_outcome - math.pi / 4, sep = " ")

def facul(t):
    fac_outcome = 1
    for i in range (1, t + 1):
        fac_outcome = fac_outcome * i
    return (fac_outcome)

def Srinivasa_Ramanujan(int_tellen):
    flt_top = 2 * math.sqrt(2)
    flt_bot = 9801
    flt_pref = flt_top / flt_bot

    flt_outcome = 0
    for k in range(int_tellen):        
        flt_outcome_top = facul(4 *k) * (1103 + 26390 * k)
        flt_outcome_bot = (facul(k) **4 ) * 396 ** (4 * k)
        flt_outcome = flt_outcome + flt_outcome_top / flt_outcome_bot
    return (flt_pref * flt_outcome)
    

def pi_zeta(inp_exponent):

    fill_zeta_outcome()
    int_outcome = 0
    for i in range(1, 1000):
        int_outcome = int_outcome + (1 / (i ** inp_exponent))

    print("Zeta ", inp_exponent)    
    print(int_outcome)
    print (flt_zeta[inp_exponent - 1])
    print("Verschil: " , int_outcome - flt_zeta[inp_exponent - 1], sep = " ")


def euler_pi_formula ():
    flt_out_come = 1 - (1 / 2 ** 2 )
    for i in range (3, 100000): 
        if isPrime(i):
            flt_out_come = flt_out_come * (1 - (1 / i ** 2 ))
    print ("Outcome: ", flt_out_come , sep = ' ')
    print ("6 / PI ^2:", 6 / math.pi ** 2)
    print ("Diff: ", flt_out_come - 6 / math.pi ** 2)


def isPrime(a):
    boven = a / 2
    teller = 2
    tst_prime = True

    while (teller <= boven and tst_prime == True):
        if a % teller == 0:
            tst_prime = False
        teller = teller + 1
    return (tst_prime)
    
def prime_formula(int_s):

    flt_outcome = 1 / 1
    for i in range(3,2000):
        if isPrime(i):
            flt_outcome = flt_outcome * (1 / (1 - i ** (-1 * int_s)))

    print(flt_outcome)
    print(pi_zeta(int_s))


