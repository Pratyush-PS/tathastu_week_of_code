size = int(input("\nEnter number of keys in the dictionary:"))
my_dict={}
for i in range(size):
    print("Key-Value #{}".format(i+1))
    key=input("Enter name of key:")
    value = int(input("Enter key value:"))
    my_dict[key] = value
    print()

print("\nOriginal dictionary is:", my_dict)

second_largest = list(sorted(my_dict.values()))[-2]

print("\nThe second largest value in the dictionary is:",second_largest)
