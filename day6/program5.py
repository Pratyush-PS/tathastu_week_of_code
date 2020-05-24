fibonnaci =list()
f,s=0,1
fibonnaci.append(f)
fibonnaci.append(s)
for i in range(50):
    t=f+s
    fibonnaci.append(t)
    f,s=s,t



size = int(input("\nEnter your sequence size:"))
seq=[]
term_sum = 0
for i in range(size):
    elem=int(input("Enter element {}:".format(i+1)))
    seq.append(elem)
    if elem in fibonnaci:
        term_sum+=elem

print("Given sequence:",seq)
print("Sum of fibonnaci elements is:",term_sum)

if(term_sum in fibonnaci):
    print("{} is a Fibonnaci Number".format(term_sum))

else:
    print("{} is not a Fibonnaci Number".format(term_sum))
