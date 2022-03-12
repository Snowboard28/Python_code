#Select negative numbers of a list

def listThings_negative():
    
    data = [[1, 5], [2 , -3, 1], [10, -1], [-8] ,[8], [10, 1], [-5, 4, 4, -2]]
    with_neg = [d for d in data if min(d) < 0]
    print( with_neg, end ='\n' )
        
    s = (1,2,3,4,5,-7,-8,-9)
    print(s, s[0], s[1], sep = ' ', end = '\n')
    with_neg = list(filter(lambda x: x<0, s))
    print (with_neg)
    
    
