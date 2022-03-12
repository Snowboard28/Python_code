def isPrime(a):
    boven = a / 2
    teller = 2
    tst_prime = True

    while (teller <= boven and tst_prime == True):
        if a % teller == 0:
            tst_prime = False
        teller = teller + 1
    return (tst_prime)
