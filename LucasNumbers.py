import math

def Lucas_Numbers (boven):
    teller = 1
    Lucas_num = [2, 1]
    
    while teller < boven:
        Lucas_num.append(Lucas_num[teller-1] + Lucas_num[teller]) 
        teller = teller + 1
    print(Lucas_num)
    

def Lucas_Numbers_X (boven):
    L_min_2 = 2
    L_min_1 = 1
    teller = 1    
    while teller < boven:
        lucas_new = L_min_2 + L_min_1
        print (lucas_new)
        L_min_2 = L_min_1
        L_min_1 = lucas_new
        teller = teller + 1
