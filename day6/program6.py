def check_s_r(arr):
    small_pos = arr.index(min(arr))
    if(arr[:small_pos]==sorted(arr[:small_pos])):
        if(arr[small_pos+1:]==sorted(arr[small_pos+1:])):
            if(arr[len(arr)-1]<arr[small_pos-1]):
                return 'YES'
    return "NO"



def main():
    size= int(input("Enter array size:"))
    num=[]
    for i in range(size):
        num.append(int(input("Enter element {}:".format(i+1))))
    
    print("\nGiven list is:",num)
    print("Is Array Sorted and Rotated:", check_s_r(num))

main()
