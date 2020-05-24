def make_palindrome(s):
    if s==s[::-1]:
        return 0
    alpha={}
    for i in s:
        alpha[i] = alpha.get(i,0)+1
    list = sorted(alpha.values())
    odd_count = [i for i in list if i%2]
    return(len(odd_count)-1)


st1= input("Enter string:")
print("Minimum deletions required:",make_palindrome(st1))         
