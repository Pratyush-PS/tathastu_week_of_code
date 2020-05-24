size= int(input("\nEnter your list size:"))
li=[]
for i in range(size):
    li.append(int(input("Enter element {}:".format(i+1))))

print("\nGiven list is:",li)
max_product=1
for i in sorted(li)[-3:]:
    max_product *=i 

print("\nMaximum possible product is:",max_product)
