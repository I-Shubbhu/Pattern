#              *
#              * *
#              * * *
#              * * * *
#              * * * * *
#              * * * * * * 

# num = int(input("Enter the number: "))
# for i in range(1,num+1): # Col
#     for j in range(1,i+1): # Row
#         print("*",end=" ")
#     print()    
    
num = int(input("Enter the number: "))
for i in range(1,num): # Col
    for j in range(1,num): # Row
        if j<=i:
            print("*",end=" ")
            
        else: print(" ",end=" ")    
    print()    
       