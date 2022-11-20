num = int(input("Enter the number : "))

if num%2==0:
    col = int(num/2)
else: col = int(num/2)+1

for i in range(1,col): # Col
    for j in range(1,num): # Row
        if j>=col+1-i and j<=col-1+i:
            print("*",end=" ")
            
        else: print(" ",end=" ")    
    print()