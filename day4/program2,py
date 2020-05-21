size = int(input("Enter the size of your list:"))
t_size = int(input("Enter the size of each tuple :"))

tup_list=[]
for i in range(size):
    list=[]
    print("\nEnter element of tuple {}:".format(i+1))
    for j in range(t_size):
        elem = input()
        list.append(elem)
    tup_list.append(tuple(list))

tup_list = tuple(tup_list)

print("\nThe given list is:", tup_list)

pos=int(input("\nEnter index to sort by(< tuple_size):"))
sorted_list = sorted(tup_list,key= lambda x: x[pos])

print("The sorted tuple list is as follows:\n",sorted_list)
