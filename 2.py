#                     * 
#                   * *
#                 * * *
#               * * * *
#             * * * * *
#           * * * * * *


num = int(input("Enter the number: "))
for i in range(1,num): # Col
    for j in range(1,num): # Row
        if j>=num-i:
            print("*",end=" ")
            
        else: print(" ",end=" ")    
    print()    
         