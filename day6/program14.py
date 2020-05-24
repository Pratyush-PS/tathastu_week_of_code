n=int(input("Enter dimension of square matrix:"))

def rotate(arr):
    for i in range(n//2):
        for j in range(i,n-i-1):
            tmp= arr[i][j]
            arr[i][j] = arr[n-1-j][i]
            arr[n-1-j][i] = arr[n-1-i][n-1-j]
            arr[n-1-i][n-1-j] = arr[j][n-1-i]
            arr[j][n-1-i] = tmp



mat=[]
for i in range(n):
    li=[]
    print("\nEnter value in row {}:".format(i+1))
    for j in range(n):
        li.append(int(input("Enter value in column {}:".format(j+1))))

    mat.append(li)

print("\nGiven Matrix is:")
for i in range(n):
    print(mat[i])
rotate(mat)
print("\nMatrix after rotation is:")
for i in range(n):
    print(mat[i])
