def replace(s):
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