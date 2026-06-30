#task 1:temperature converter
'''
celsius=float(input("enter temp in celsius"))
time=int(input("enter time:"))
farenheit=celsius*1.8+32
print("temperature in farenheit:",farenheit)
'''

#task 2:simple interest calculator
'''
principal=int(input("enter principal amount:"))
rate=int(input("enter the rate:"))
time=int(input("enter time:"))
si=principal*rate*time/100
print("simple interest:",si)
'''

#task 3:square and cube generator
'''
number=int(input("enter the whole number"))
square=number**2
cube=number**3
print("square:",square)
print("cube:",cube)
'''

#task 4:total minutes & seconds
'''
hours=float(input("enter the duration in hours"))
minutes=hours*60
seconds=hours*3600
print("enter minutes:",minutes)
print("enter seconds:",seconds)
'''

#task 5:average of three marks
'''
tamil=int(input("enter tamil"))
english=int(input("enter english"))
maths=int(input("enter maths"))
total=tamil+english+maths
average=total/3
print("total:",total)
print("average:",average)
'''
#task 6:digits extractor
'''
num=int(input("enter 3 digit number"))
first=num//100
second=(num//10)%10
third=num%10
print("first digit:",first)
print("second digit:",second)
print("third digit:",third)
'''

#task 7:swap without a third variable using bitwise operators
'''
a=int(input("enter a value:"))
b=int(input("enter b value"))
a=a^b
b=a^b
a=a^b
print("a=",a)
print("b=",b)
'''

#task 8:the atm cashier breakdown
'''
amount=int(input("enter amount:"))
five_hundred= amount//500
remaining= amount%500
hundred=remaining//100
print("500 notes:",five_hundred)
print("100 notes:",hundred)
'''

#task 9:weeks and lefover days breakdown
'''
days=int(input("enter total number of days:"))
weeks=days//7
leftover_days=days%7
print("no of weeks:",weeks)
print("no of days left:",leftover_days)
'''

#task 10:reverse a 2-digit number mathematically
'''
number=int(input("enter 2-digit number:"))
last_digit=number%10
first_digit=number//10
reverse=(last_digit*10)+first_digit
print("reversed number=",reverse)
'''
