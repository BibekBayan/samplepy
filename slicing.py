'''def slicing(st,ind):
    my_st = st.split()
    
    if len(my_st)<ind:
        print("Index out of range")
    else:
        
        for i in range(0,len(my_st)):
            print(i)
            if i==len(my_st):
                break
            
            
st = input()
ind= int(input())

slicing(st,ind)
'''

'''def slicing(st,ind):
    
    my_st=list(st)
    if len(my_st)>=ind:
        for i in range(1,len(my_st),2):
            print(my_st[i], end='')
        
    else:
        print("Index out of range")
        
st = input()
ind = int(input())

slicing(st,ind)
'''

'''def odd_ind(str1):
    my_st = list(str1)
    if 
    
'''

'''def decimal(n):
    num_0 = 10**(n-1)
    num = n//num_0
    print("{:.2f}".format(num))
    
n = int(input())

decimal(n)

'''

'''def replace(s):
    s_list=list(s)
    f_list=[]
    l_list=[]
    
    for i in s_list:
        if i.isupper():
            f_list.append(i)
        elif i.islower():
            l_list.append(i)
        
    print(f_list)
    print(l_list)
    
    fi_list=f_list+l_list
    
    for element in fi_list:
        print(element, end='')
    
    
s = input()            
replace(s)
'''

'''s1 = input()
s2 = input()

s3 = s1+s2
print(s3)

m=len(s3) // 2

print(s3[:m]+s1+s3[m:])
'''

'''s = input()

m = len(s) // 2

print(s[m] + s[len(s)-1])
'''

s1=input()

s2=input()


if s2 in s1:
    print("True")
        
else:
    print("False")
        





