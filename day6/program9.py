size = int(input("\nEnter size of your list:"))
list=[]
for i in range(size):
    list.append(int(input("Enter element {}:".format(i+1))))

print("\nThe given list is:",list)

k= int(input("\nEnter value of k:"))

sort = sorted(list)

print("\nThe kth smallest value in list is=",sort[k-1])
