
import sys
sys.setrecursionlimit(10**6)


def fact(n): 
  
    if(n == 0): 
        return 1
  
    return n * fact(n - 1) 
  

def fact1(n):
    f = 1
    for x in range(1, n + 1):
        f *= x
    print("Factorial ", n,  " : " , f)
    
    
