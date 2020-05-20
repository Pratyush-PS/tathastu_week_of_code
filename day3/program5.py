size1,size2 = int(input("\nEnter size of list 1:")),int(input("Enter size of list 2:"))
list1,list2=[],[]

print("\nEnter elements of 1st list:")
for i in range(size1):
    elem=int(input())
    list1.append(elem)


print("\nEnter elements of 2nd list:")
for i in range(size2):
    elem=int(input())
    list2.append(elem)


print("The original lists are:\nList1={} \n List2={}".format(list1,list2))

intersect = list(set(list1).intersection(set(list2)))
print("The intersection of both lists are:",intersect)
