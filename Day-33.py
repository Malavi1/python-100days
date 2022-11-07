 # sum of digits
 
def sum_all(n):
    if  n == 0:
        return n
    return n + sum_all(n-1)
print(sum_all(2))

#prime numbers in the range

def prime_range(n1, n2):
    result = []
    for i in range(n1, n2+1):
        if i == 1:
            continue
        c=0
        for j in range(2, i//2+1):
            if i%j == 0:
                c+=1 
        if c == 0:
            result.append(i)
    return result
print(prime_range(1,21))
            
        
