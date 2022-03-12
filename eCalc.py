from math import factorial
from math import exp
import decimal

e_const = 2.71828182845904523536028747135266249775724709369995


def e_main_calc_2():
    factorial = 1.000000000000000000
    e = 1.0000000000000000000000000000000
    for n in range (1,20):
        factorial = factorial * n
        e = e + (1 / factorial)
        print ("Step: ", n, "E: ", e , "    Factorial", factorial)
        
    print(e)


def e_main_calc():
   
    e_input_precision = 50

    decimal.getcontext().prec = e_input_precision
    
    print ("0", decimal.Decimal(e_const))

    print ("1", eCalc(e_input_precision) , "Verschil:", eCalc(e_input_precision) - decimal.Decimal(e_const) )

    print("2", str (compute_e(e_input_precision))[:e_input_precision + 1] , "Verschil:", compute_e(e_input_precision) - decimal.Decimal(e_const))

    print ("3", e_number_of_places(), "Verschil:", e_number_of_places() - decimal.Decimal(e_const))
    print ("Error max" , 1 / factorial (e_input_precision)) 
 

def eCalc(n):
   
    e_iterations = n
    e_power = 1
    e_sofar = [1]

    for i in range (1, e_iterations + 1):
        counter = e_power ** i
        denominator = factorial(i)
        e_sofar.append(e_sofar[i - 1] + decimal.Decimal(counter / denominator))
    if e_iterations < 10:
        print  ("E_sofar:",  e_sofar, "\n")
        print(e_sofar)
    return e_sofar[i]

# https://github.com/microice333/Python-projects/blob/master/n_digit_e.py
# find e to nth digit by brothers' formulae: http://www.intmath.com/exponential-logarithmic-functions/calculating-e.php
def factorialX(n):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(factorials[i - 1] * i)
    return factorials


def compute_e(n):
    print("E: ", e_const)
    decimal.getcontext().prec = n + 1
    e = 2
    e_float = 2
    factorials = factorialX(2 * n + 1)
    for i in range(1, n + 1):
        counter = 2 * i + 2
        denominator = factorials[2 * i + 1]
        e += decimal.Decimal(counter / denominator)
    e_float = float(e)
    print ("Diff: ", e_const - e_float )
    return e

def start_e():
#     e_const = 2.71828182845904523536028747135266249775724709369995
    while True:
        n = int(input("Please type number between 0-1000: "))
        if n >= 0 and n <= 1000:
            break

    print(str (compute_e(n))[:n + 1])
    print(decimal.Decimal(exp(1)))
    print(str (compute_e(n) - decimal.Decimal(exp(1)))[:n + 1])
    print(str (compute_e(n) - decimal.Decimal(e_const) )[:n + 1])
          
def e_number_of_places():
    import decimal  # Use of decimal module due to increased precision compared to float()

    factorial = 1  # The factorial is defined as 1 in order to find e from a nested series.

    e = 2  # e is defined as 2 in order to begin the sequence of 2.xxxx.

    for number in range(2, 50): # The larger the range, the higher degree of accuracy for euler's number.
                                # The two lines below perform the nested series calculation in order to find e.
        factorial *= number
        e += decimal.Decimal(1.0) / decimal.Decimal(factorial)
    return(e)
    
def test_e():
    e = 1
    factorial = 1

    for n in range(1, 20):
       factorial *= n
       e += 1 / factorial
       print(n, e , e_const, e - e_const, 1 / factorial)
