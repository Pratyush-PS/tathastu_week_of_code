def sortEvenOdd(li):
    even = [i for i in li if i%2==0]
    odd = [i for i in li if i%2]
    sorted_list = sorted(odd,reverse=True)+sorted(even)
    return sorted_list


size = int(input("Enter list size:"))
num_list=[]
for i in range(size):
    num_list.append(int(input("Enter element {}:".format(i+1))))

print("\nOriginal List={}\n Sorted List={}".format(num_list,sortEvenOdd(num_list)))
