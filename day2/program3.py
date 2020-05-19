n= int(input("Enter number of level:"))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"+(" "*2*(i-1))+"*")

for i in range(1,n+1):
    print(" "*(n-i)+"*"+ " "*2*(i-1)+ "*")
    
