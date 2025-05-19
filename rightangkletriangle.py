# right angled triangle
n = int(input("Number of rows: "))
#outer loop to handle no of rows
for i in range(n): # 1 end till 5
    #inner loop to handle no of columns
    for j in range(i+1): #range(2)
        print("*",end=" ")
    print()