import math
import time

def twin_primes(boven, inc_teller):
    teller = 2
    tst_prime = True

#     inc_teller = 4
    
    if inc_teller == 2:
        print_str = "Twin";
    elif inc_teller == 4:
        print_str = "Cousin";
    elif inc_teller == 6:
        print_str = "Sexy";
    else:
        print_str = "Unknown"
        
    print("Start",print_str ,"prime:", time.asctime( time.localtime(time.time()) ))
    while (teller <= boven):
        if isPrime(teller) and isPrime (teller + inc_teller):
                print (print_str ,"prime:",teller,teller + inc_teller)
        teller = teller + 1
    print("End",print_str ,"prime:", time.asctime( time.localtime(time.time()) ))



def isPrime(a):
    boven = a / 2
    teller = 2
    tst_prime = True

    while (teller <= boven and tst_prime == True):
        if a % teller == 0:
            tst_prime = False
        teller = teller + 1
    return (tst_prime)
    
    
def instgram_q_p():
    lcl_teller = 2
    lcl_boven_grens = 140
    lcl_candidate = 1
    
    while lcl_teller < lcl_boven_grens:
        if isPrime(lcl_teller):
            lcl_candidate = lcl_teller ** lcl_teller + 2
            if isPrime(lcl_candidate):
                print("We have a winner: ", lcl_teller, " " ,lcl_candidate)
            else:
                print("Helaas ",lcl_teller, " " ,lcl_candidate)
        lcl_teller = lcl_teller + 1
    return 

def housekeeping(int_input_1):
    print("Start: ", time.asctime( time.localtime(time.time()) ))
    print ("Input: ", int_input_1)
    factor = []
    ontbind_prime(int_input_1, factor)
    print (factor)
    print("End: ", time.asctime( time.localtime(time.time()) ))



def ontbind_prime(int_input, loc_factor):
    boven = int_input / 2
    teller = 2
    inc_teller = 1
    tst_prime = True
    
    while (teller <= boven and tst_prime == True):
        if teller % 10000005 == 0:
            print ("Input: ", int_input, " teller: " , teller)
        if int_input % teller == 0:
            tst_prime = False
#            print(" ", teller)
            loc_factor.append(teller)
#            print(loc_factor) 
            ontbind_prime(int_input / teller, loc_factor)
        teller = teller + inc_teller
    if tst_prime == True:
#        print (" ", int(int_input))
        loc_factor.append(int(int_input))

    return


def instagram_puzzel():
    p = 2
    boven = 20
    while p < boven:
        if isPrime(p):
            q = (2019**p - 27**p) / p
 #            if int(q) == q:
            print ("Teller: ",p," q: ", int(q))
        p = p + 1


def zeef_van_eratosthenes():
    n = 100
    s = list(range(1, n + 1))
    print (len(s) )
    
    p = 2
    while p < n / 2:
        for i in range(2 * p, n + 1, p):
            s[i - 1] = 0
        new_candidate  = False
        i = 1
        while i < n and new_candidate == False:
            if s[i]>p:
                p = s[i]
                new_candidate = True
            i = i + 1
    s = list(filter(lambda x: x != 0, s))
    print (s)
