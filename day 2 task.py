# 1)student pass or fail
'''
m=int(input("enter your mark:"))
if m>=35:
    print("pass")
else:
    print("fail")
'''

#2)check voting eligibility
'''
a=int(input("enter your age:"))
if a>=18:
      print("you are eligible to vote")
else:
    print("not eligible")
'''


#3)calculate the customer final amount
'''
amount=5000
d=10
final=amount*d/100
print("final amount:",final)
'''

#4)verify the password
'''
s_pass=1234
p=int(input("enter your password:"))
if p==s_pass:
      print("you can access a website")
else:
    print("wrong password")
'''

#5)based on marks
'''
m=int(input("enter your marks:"))
if m>=90:
      print("A grade")
elif m>=75:
    print("B grade")
elif m>=50 :
    print("C grade")
else:
    print("fail")
'''

#6)Simple calculator
'''
a=int(input("enter your a:"))
b=int(input("enter your b:"))
add=a+b
sub=a-b
mul=a*b
div=a/b
print("addition:",add)
print("subtraction:",sub)
print("multiplilcation:",mul)
print("Division:",div)
'''

#7)Calculate electricity charges
'''
u=int(input("enter you units:"))
if u<=101:
      print("₹2/unit")
elif u<=200:
      print("₹3/unit")
elif u>200:
    print("₹5/unit")
else:
    print("enter correct units:")
'''

#8)ticket fare based on age
'''
a=int(input("enter your age:"))
if a<5:
    print("Ticket free")
elif a<12:
    print("Ticket price 50")
elif a>=12:
    print("Ticket price 100")
else:
    print("enter your age correct")
'''

#9) bank approves a loan
'''
a=int(input("enter you amount:"))
c=int(input("enter you credit score:"))
if a>=30000 and c>=700:
      print("Eligible for loan approved")
else:
    print(" Not Eligible")
'''

#10)student is eligible for college admission
a=int(input("enter your academics score:"))
e=int(input("enter hour entrance score:"))
if a>60 and a>70:
    print("Eligible for college admission")
else:
    print("not eligible")
    #11)A company recruits candidates check eligible or not
'''
d=int(input("enter your degree %:"))
a=int(input("enter your aptitude Score:"))
if d>65 and a>75:
    print("eligible to attend next round")
else:
    print("not eligible")
'''

#12)A scholarship is awarded for student to check eligibe or not
'''
s=int(input("enter your score:"))
a=int(input("enter your attendance %"))
if s>80 and a>75:
    print("eligible for scholarship")
else:
    print("not eligible")
'''

#13)check the user and pin atm efficient balance
'''
amount=1000
a=int(input("enter your amount:"))
if a<=amount:
    pin=int(input("enter your pin:"))
    if pin==1234:
      print("payment processing")
    else:
        print("wrong pin")
else:
    print("insufficent balance")
'''

#14)verify the username and password
'''
user="jothi"
password=4567
u=str(input("enter your username:"))
p=int(input("enter your password:"))
if user==u and password==p:
    print("generating otp")
else:
    print("invalid username or password")
'''

#15)check the doctor is available
'''
doctor="gopi"
d=str(input("enter doctor name:"))
if doctor==d:
    s=int(input("enter the slots"))
    if s==2:
        print("you had appoinement")
    else:
        print("not")
else:
    print("doctor not available")
'''

#16)checking student can access the cybersecurity lab
'''
r=int(input("enter the register no:"))
if r>100:
    c=int(input("enter your course fees:"))
    if c==35000:
          print("you can access the lab")
    else:
          print(" fees balance")
else:
    print("invalid reg")
'''

#17)employee is eligible
'''
e=int(input("enter your experience:"))
if e>3:
    r=int(input("enter your ratings:"))
    if r>8:
        print("your are eligible")
    else:
        print("rating less")
else:
    print("experience is less")
'''

#18)checking fees detail for an online examination portal 
'''
fees=90000
f=int(input("enter your fees:"))
if fees==f:
    print("hall ticket is available")
else:
    print("fees not cleared")
'''

#19) A hostel room can be allotted only if the student has been selected for admission
'''
a=int(input("enter your admission no:"))
if a>100:
    print("you are alloted by hotel")
else:
    print("you not selected by admission")
'''

#20)An online shopping website offers:
amount=5000
a=int(input("enter your amount:"))
if a>5000:
    print("20% discount for premium members")
elif a>1000:
    print("10% discount for non-premium members")
else:
    print("no discounts")
