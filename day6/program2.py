size= int(input("\nEnter size of list:"))
print("\nEnter list elements(0/1):")
list=[]
for i in range(size):
    list.append(int(input()))

print("Original list={}\nSorted List={}".format(list,sorted(list)))
