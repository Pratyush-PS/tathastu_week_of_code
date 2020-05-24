size = int(input("\nEnter size of your list:"))
list=[]
for i in range(size):
    list.append(int(input("Enter element {}:".format(i+1))))

print("\nThe given list is:",list)

for i in range(max(list)+1):
    if i not in list:
        print("Smallest missing number is:",i)
        break
