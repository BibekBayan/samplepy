def decimal(n):
    num_0 = 10**(n-1)
    num = n//num_0
    print("{:.2f}".format(num))
    
n = int(input())

decimal(n)