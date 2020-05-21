n = int(input("Enter tuple size:"))
tup=[]
print("\nEnter elements in your tuple:")
for i in range(n):
    elem = input()
    tup.append(elem)

tup=tuple(tup)
print("The given tuple is:",tup)

var = input("Enter element to be counted:")

count = len([i for i in tup if i==var])
print("\nThe element occurs {} times in the tuple".format(count))
