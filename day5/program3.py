def stolen_values(house_list):
    if(len(house_list)==2):
        return(max(house_list))
    elif (len(house_list)==1):
        return house_list[0]
    
    elif len(house_list)==3:
        return max(house_list[1], house_list[0]+house_list[2]))

    return max(house_list[0]+stolen_values(house_list[2:]), house_list[1]+stolen_values(house_list[3:]))



size = int(input("Enter numbers of houses: "))
val=[]
for i in range(size):
    val.append(int(input("Enter value in house {}:".format(i+1))))

print("\nGiven house values:",val)

print("Maximum possible stolen value is:",stolen_values(val))
