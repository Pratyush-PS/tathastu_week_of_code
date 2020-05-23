def with_largest(num,size):
    list=num.copy()
    for i in range(size-1):
        list[i] = max(num[i+1:])
    return list


size= int(input('\nEnter list size:'))

my=[]

for i in range(size):
    elem = int(input())
    my.append(elem)


print("\nInitial list:",my)


print("Replacing with :",with_largest(my,size))
