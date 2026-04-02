def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a_new=a[2:][::-1]
    b_new=b[2:][::-1]
    
    total=0
    result=''
    
    for i in range(len(a_new)):
        
        if a_new[i]=='1':
            total+=2**i
    
    
    for j in range(len(b_new)):
        
        if b_new[j]=='1':
            total+=2**j
            
    if total==0:
        return "0b0"
    
    
    while total > 0:
        result += str(total % 2)
        total //= 2
        
    return "0b" + result[::-1]