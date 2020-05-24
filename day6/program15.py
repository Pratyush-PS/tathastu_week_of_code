size = int(input("\nEnter sizeof list:"))

def count_ind(num):
    for i in range(size):
        s=0
        if (i!=0):
            for j in range(i):
                if num[j]>num[i]:
                    s=1
                    break
        if(i!=size-1):
            for k in range(i+1,size):
                if num[i]>num[k]:
                    s=1
                    break
        if(s==0):
            return num[i]
    return "No such value"


li=[]
for i in range(size):
    li.append(int(input('Enter element {}:'.format(i+1))))

print("Given list is:",li)

print("\nThe partition value in array is:",count_ind(li))
