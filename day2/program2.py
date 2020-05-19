n= int(input("Enter number of terms in your series:"))

print("The Fibbonaci series is:")

f,s=0,1
print(f,s,end=" ")

for i in range(1,n-1):
    t=f+s
    print(t,end=" ")
    f,s= s,t
    
