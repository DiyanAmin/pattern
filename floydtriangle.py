#Printing Floyd Triangle
val=1
rows=int(input('Number of rows: '))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(val,end=' ')
        val+=1
    print()