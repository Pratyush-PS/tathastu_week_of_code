#METHOD 1
def method1(l):
    return list(set(l))


#Method 2
def method2(l):
    copy_list =[]
    for i in l:
        if i not in copy_list:
            copy_list.append(i)

    return copy_list


size= int(input("\nEnter list size:"))
my_list = []
print("\nEnter list elements:")
for  i in range(size):
    elem = input("Element {}:".format(i+1))
    my_list.append(elem)

print("\nOriginal list:",my_list)    
print("\nList after removing duplicates :\nFrom Method 1:",method1(my_list))
print("\nBy Method 2:",method2(my_list))
