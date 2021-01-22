def FactorSum(x, o):
    
    t = 0
    
    
    for i in range (0, x + 1):
        t = t + i
    

   
    a = 1
   
    for i in range (1, x + 1):
        a = a * i


    

    if o == "Sum":
        return t
    else:
        return a

print(FactorSum(10, "Sum"))