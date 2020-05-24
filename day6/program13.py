size = int(input("\nEnter size of your list:"))
list=[]
for i in range(size):
    list.append(float(input("Enter element {}:".format(i+1))))

print("\nThe given list is:",list)

s=0
for i in range(size-2):
    for j in range(i+1,size-1):
        for k in range(i+2,size):
            sum = list[i]+list[j]+list[k]
            if 0<sum<1:
                s=1
                print("The required triplet is: ({}, {}, {}), with sum={}".format(list[i],list[j],list[k],sum))

if s==0:
    print("No such triplet exists")
