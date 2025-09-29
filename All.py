# 1 . Write a program to check if a number is even or odd.

num = int(input ("enter a number: "))
if num % 2== 0:
    print (f" {num} is even .")
else:
    print (f" {num} is odd .")

# 2. Write a program to find the largest of three numbers.

x=int(input("Enter First Number:"))
y=int(input("Enter Second  Number:"))
z=int(input("Enter Third  Number:"))
if x>y and x>z:
    print(x, "is the largest number")
elif y>x and y>z:
    print(y,"is the largest number")
else:
     print(z,"is the largest number")

# 3. Write a program to reverse a string without using slicing.

n=input("Enter a String: ")
str_rev =""
for i in range (len(n)-1,-1,-1):
    str_rev+=n[i]
print(str_rev)

# 4 . Write a program to check if a string is a palindrome.

s=input("Enter a String:")
s= s.lower()
rev=s[::-1]
if s==rev:
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")

# 5. Write a program to count vowels and consonants in a string.

s=input("Enter the String: ")
vowels=0
consonants=0
for i in s:
    if i in'aeiou':
        vowels+=1
    else:
        consonants+=1
print("vowels:",vowels,"\nconsonants: ",consonants)


# 6 . Write a program to find factorial of a number (using loop and recursion)

n=int(input("Enter the number: "))
s=1
for i in range(n,0,-1):
    s*=i
print(s)


# 7 . Write a program to generate Fibonacci series up to n terms.

n = int(input("enter the number: "))
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci(n)

# 8. Write a program to swap two numbers without using a third variable.

n = int(input("Enter first number: "))
x = int(input("Enter second number: "))
n,x =x,n
print(f"After swapping n,x=",n,",",x)


# 9. Write a program to find the sum of digits of a number.

n=input("Enter the numbers:")
sum=0
for i in n:
    sum+=int(i)
print("Sum of Digits :",sum)    


# 10. Write a program to find the second largest number in a list.

n= [10,12,8,9,4,20,53,60]
small = large = n[0]
for num in n:
    if num < small:
        small = num
    if num > large:
        large = num
sd_le = small  
for num in n:
    if large > num > sd_le:
        sd_le = num
print("Second largest :", sd_le)


# 11. Write a program to remove duplicates from a list.

n=[3,2,6,7,9,10,7,8,10,6,5]
list=[]
for i in n:
    if i not in list:
        list.append(i)
print(f'List without duplicate :{list} ')


# 12. Write a program to find common elements in two lists.

x=[3,7,8,9,4,6]
y=[4,5,7,8,9,6]
n=[]
for i in x:
    for j in y:
        if i==j:
            n.append(i)
print("Common members:",n)

# 13. Write a program to sort a list without using sort().


n = [5,2,8,4,3,1]
s_n = n.copy()

n = len(s_n)
for i in range(n):
    for j in range(0, n-i-1):
        if s_n[j] > s_n[j+1]:
            
            s_n[j], s_n[j+1] = s_n[j+1], s_n[j]

print(f"Original: {n}")
print(f"Sorted: {s_n}")


# 14. Write a program to check if two strings are anagrams.

x=input("enter a string: ")
y=input("enter a string: ")
if sorted(x)==sorted(y):
    print("These are Anagrams")
else:
    print("These are not Anagrams")


# 15. Write a program to count the frequency of words in a given string.

x="Hello! Neha is here"
n=x.split()
frequency={}
for i in n:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)            


# 16. Write a program to merge two dictionaries.

dictionary1= {'a':30, 'b':34}
dictionary2= {'c':90, 'd':26}
dictionary1.update(dictionary2)
print(dictionary1)

#17. Write a program to find all prime numbers between 1 and 100.

for n in range(2,101):
    p_n=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            p_n=False
    if p_n:
            print(n,end=" ")


# 18. Write a program to find the GCD and LCM of two numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
a =num1
b = num2
while b != 0:
    temp = b
    b = a % b
    a = temp
gcd = a
lcm = (num1 * num2) // gcd
print("LCM of {}, {} = {}".format(num1, num2, lcm))
print("GCD of {}, {} = {}".format(num1, num2, gcd))

# 19. Write a program to find missing number in a list of 1 to n.

print("Enter numbers:")
num = list(map(int, input().split()))
n = len(num) + 1
total = n * (n + 1) // 2
actual = sum(num)
missing = total - actual
print(f"Missing number is: {missing}")



# 20. Write a program to check if a number is an Armstrong number.

n = int(input("Enter a number: "))
temp = n
digits = 0
while temp > 0:
    digits += 1
    temp //= 10
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10
if sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
