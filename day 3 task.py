 # task 1

'''#
for i in range (7):
     print ("vishrudh")

# task 2
#
for i in range (1,21):
     print (i)

# task 3
#
for i in range (20,0,-1):
    print (i)

# task 4
#
for i in range (2,51,2):
    print (i)

# task 5
#
for i in range (1,51,2):
    print (i)

# task 6
#
sum=70
for i in range (1,11):
    sum +=1
print("sum=",sum)
# task 7
#
num =int(input("enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
# task 8
#
name = input("enter a name:")
count= len(name)
print("Number of letter=",count)'''
#task 9
#
word = input("enter a word:")
for ch in word:
    print(ch)

#task 10
#
word = input("enter a word:")
count=0
for ch in word.lower():
    if ch in "aeiou":
        count +=1
print("number of vowels=",count)

#task 11
#
n=5
for i in range (n):
    for j in range (n):
        if i==j or i+j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()