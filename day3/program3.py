def remove_duplicates(s):
    copy_str=""
    for i in s:
        if i not in copy_str:
            copy_str +=i
    return(copy_str)


str1 = input("Enter your string:")

print("The string without duplicates are:", remove_duplicates(str1))
