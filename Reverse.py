
def reverse_number(int_input):
    reverse = 0

    teller = int_input

    while teller > 0:
        rest = teller % 10
        reverse = reverse * 10 + rest
        teller = int(teller / 10)
    print ("Reverse: ", reverse)
    

    
