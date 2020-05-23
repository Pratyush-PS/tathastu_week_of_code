def replace_digits(n):
    i = str(n).replace('0','5')
    return int(i)


n= int(input("\nEnter a number:"))
print("\nAfter replacing '0' with '5':",replace_digits(n))
