def knapsack(knap_weight, item_list):
    if knap_weight==0 or len(item_list)==0:
        return 0
    if(len(item_list)==1):
        if(item_list[0][0]>knap_weight):
            return 0
        return item_list[0][1]
    if item_list[0][0]>knap_weight:
        return knapsack(knap_weight,item_list[1:])
    return max(item_list[0][1]+knapsack(knap_weight-item_list[0][0],item_list[1:]),knapsack(knap_weight,item_list[1:]))






weight = int(input("Enter weight of knapsack:"))
size = int(input("\nEnter number of items:"))
list=[]

for i in range(size):
    print()
    print("Enter for item {}".format(i+1))
    item_weight=int(input("Weight:"))
    item_value=int(input("Value:"))
    list.append((item_weight,item_value))

print("\n The given weight and values lists are:")
for i in range(size):
    print()
    print("Item {}".format(i+1))
    print(list[i])


print("\nMaximum possible stolen value is:",knapsack(weight,list))

