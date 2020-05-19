def even_odd(n):
    if(n%2==0):
        return 'Even'
    else:
        return 'Odd'


def isPrime(n):
    for i in range(2,n//2):
        if n%i==0:
            return 'No'
    return 'Yes'


def isPalindrome(n):
    rev_num = int(str(n)[::-1])
    if(rev_num==n):
        return 'Yes'
    else:
        return 'No'


def isArmstrong(n):
    num,sum=n,0
    num_digits = len(str(n))
    while(num>0):
        rem=num%10
        sum+=(rem**num_digits)
        num//=10
    if(n==sum):
        return 'Yes'
    else: return 'No'


number = int(input("Enter a number:"))

print("Odd or Even:",even_odd(number))
print("Is a Prime Number:",isPrime(number))
print("Is a Palindrome:",isPalindrome(number))
print("Is Armstrong:",isArmstrong(number))
    
        
