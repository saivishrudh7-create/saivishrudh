#task 1
i=1
while i<=10:
    print(i)
    i+=1
#task 2
i=10
while i>=1:
    print(i)
    i-=1
#task 3
i=2
while i<=20:
    print(i)
    i+=2
#task 4
i=1
while i<=20:
    print(1)
    i+=2
#task 5
i=1
total=0

while i<=50:
    total +=i
    i+=1

print("sum=",total)
#task 6
number=int(input("Enter a number:"))
i=1

while i<=10:
    print(number,"x",i,"=",number*i)
    i+=1
#task 7
number=int(input("Enter a number:"))
count=0

while number>0:
    count+=1
    number//=10

print("Digits=",count)
#task 8

number=int(input("Enter a number:"))
reverse=0

while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number//=10

print("Reverse=",reverse)
#task 9

number=int(input("Enter a number:"))
temp=number
reverse=0

while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10

if number==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#task 10

number=int(input("Enter a number:"))
temp=number
sum_digits=0
product=1

while temp>0:
    digit=temp%10
    sum_digits+=digit
    product*=digit
    temp//=10

if sum_digits==product:
    print("spy number")
else:
    print("Not a Spy Number")

#task 11
    
number=int(input("Enter a number:"))
product=1

while number>0:
    digit=number%10
    product*=digit
    number//=10

print("Sum of digits=",sum_digits)

#task 12

number=int(input("Enter a number:"))
product=1

while number>0:
    digit=number%10
    product*=digit
    number//=10

print("Product=",product)

#task 13

num=int(input("Enter a number:"))
temp=num
digits=len(str(num))
total=0

while temp>0:
    digit=temp%10
    total+=digit**digits
    temp//=10

if total==num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#task 14

num=int(input("Enter a number:"))
largest=0

while num>0:
    digit=num%10
    if digit<smallest:
        smallest=digit
    num//=10

print("Smallest digit=",smallest)

#task 15

num=int(input("Enter a number:"))
smallest=9

while num>0:
    digit=num%10
    if digit<smallest:
        smallest=digit
    num//=10

print("Smallest digit=",smallest)

#task 16

n=int(input("Enter a number of terms:"))

a=0
b=1
count=1

while count <=n:
    print(a,end="")
    c=a=b
    a=b
    b=c
    count +=1

#task 17

num=int(input("Enter a number:"))
fact=1
i=1

while i<=num:
    fact*=i
    i+=1

print("Factorial=",fact)
