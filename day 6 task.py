numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

numbers = [12, 45, 7, 89, 23, 56]

print("Largest:", max(numbers))
print("Smallest:", min(numbers))

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

numbers = [10, 20, 10, 30, 20, 40, 50]

unique = list(set(numbers))

print("List without duplicates:", unique)

numbers = [12, 45, 7, 89, 23, 56]

numbers.sort()

print("Second largest:", numbers[-2])

numbers = [1, 2, 3, 4, 5]

reversed_list = numbers[::-1]

print("Reversed list:", reversed_list)

list1 = [5, 2, 8]
list2 = [1, 7, 3]

merged = list1 + list2
merged.sort()

print("Merged and sorted list:", merged)

numbers = [10, 20, 10, 30, 10, 40]

element = 10

count = numbers.count(element)

print(element, "appears", count, "times")

numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

students = ["Sai", "Rahul", "Priya", "Anu", "Karthik"]

name = input("Enter student name: ")

if name in students:
    print(name, "is found.")
else:
    print(name, "is not found.")



subjects = ("Math", "English", "Science", "Python", "History")

for subject in subjects:
    print(subject)

subjects = ("Math", "English", "Science", "Python", "History")

print("Length:", len(subjects))

numbers = (10, 20, 30, 20, 40, 20)

print("Count of 20:", numbers.count(20))

subjects = ("Math", "English", "Science", "Python", "History")

print("Index of Python:", subjects.index("Python"))

subjects = ("Math", "English", "Science")

subject_list = list(subjects)
subject_list.append("Python")

print(subject_list)

numbers = (45, 78, 23, 90, 56)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)

subjects = ("Math", "English", "Science")

if "Science" in subjects:
    print("Element found")
else:
    print("Element not found")

marks = [80, 75, 90, 85, 95]

marks_tuple = tuple(marks)

average = sum(marks_tuple) / len(marks_tuple)

print("Tuple:", marks_tuple)
print("Average:", average)

numbers = (10, 20, 30, 40, 50)

print("First:", numbers[0])
print("Middle:", numbers[len(numbers) // 2])
print("Last:", numbers[-1])


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1 & set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

print(set1 - set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 ^ set2)

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))
print(unique)

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))

set1 = {1, 2, 3, 4}
set2 = {2, 3}

print(set1.issuperset(set2))

fruits = {"apple", "banana"}

fruits.add("mango")
fruits.remove("banana")

print(fruits)

classA = {"Arun", "Bala", "Kiran", "Rahul"}
classB = {"Kiran", "Rahul", "Vijay"}

common = classA & classB
print(common)

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))



student = {
    "name": "Sai",
    "age": 18,
    "course": "ECE",
    "mark": 95
}

print(student)

student = {"name": "Sai", "age": 18}

student["city"] = "Salem"

print(student)

student = {"name": "Sai", "mark": 85}

student["mark"] = 95

print(student)

student = {
    "name": "Sai",
    "age": 18,
    "mark": 95
}

del student["age"]

print(student)

student = {
    "name": "Sai",
    "age": 18,
    "mark": 95
}

print(student.keys())

student = {
    "name": "Sai",
    "age": 18,
    "mark": 95
}

print(student.values())

student = {
    "name": "Sai",
    "age": 18
}

if "age" in student:
    print("Key exists")
else:
    print("Key does not exist")

text = "python"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

marks = {
    "Sai": 95,
    "Rahul": 88,
    "Anu": 91,
    "Kiran": 97
}

top_student = max(marks, key=marks.get)

print("Top Student:", top_student)
print("Mark:", marks[top_student])

dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c"}



cart = []

cart.append("Milk")
cart.append("Bread")
cart.append("Eggs")

print("Cart:", cart)

cart.remove("Bread")

print("Updated Cart:", cart)

attendance = ["Arun", "Bala", "Kiran", "Sai"]

name = input("Enter student name: ")

if name in attendance:
    print(name, "is present")
else:
    print(name, "is absent")

days = ("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday")

n = int(input("Enter day number (1-7): "))

print(days[n-1])

gps = (11.6643, 78.1460)

print("Latitude:", gps[0])
print("Longitude:", gps[1])

visitors = set()

visitors.add(101)
visitors.add(102)
visitors.add(103)
visitors.add(101)

print("Unique Visitors:", visitors)

student1 = {"Python", "Java", "C"}
student2 = {"Python", "C++", "Java"}

print("Common Courses:", student1.intersection(student2))

employees = {
    101: {"Name": "Arun", "Department": "HR", "Salary": 30000},
    102: {"Name": "Bala", "Department": "IT", "Salary": 50000}
}

print(employees)

contacts = {
    "Arun": "9876543210",
    "Bala": "9123456789"
}

name = input("Enter name: ")

if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")

marks = {
    "Arun": 85,
    "Bala": 92,
    "Sai": 88
}

topper = max(marks, key=marks.get)
print("Topper:", topper, "-", marks[topper])

marks["Sai"] = 95

print("Updated Marks:", marks)

library = {
    1: "Python Basics",
    2: "Java Programming",
    3: "Data Structures"
}

book_id = int(input("Enter Book ID: "))

if book_id in library:
    print("Book:", library[book_id])
else:
    print("Book not found")


lst = [1, 2, 3, 4]

tup = tuple(lst)
st = set(tup)
d = {i: i*i for i in st}

print("List:", lst)
print("Tuple:", tup)
print("Set:", st)
print("Dictionary:", d)

numbers = [1, 2, 3, 2, 4, 5, 3, 6]

count = {}

for i in numbers:
    count[i] = count.get(i, 0) + 1

print("Duplicates:")
for key, value in count.items():
    if value > 1:
        print(key)

sentence = input("Enter a sentence: ")

words = sentence.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = set(list1).intersection(set(list2))

print("Common Elements:", common)

students = ["Arun", "Bala", "Sai"]        # List
roll_no = (101, 102, 103)                 # Tuple
subjects = {"Python", "Java", "C"}        # Set
marks = {"Arun": 85, "Bala": 90, "Sai": 95}  # Dictionary

print("Students:", students)
print("Roll Numbers:", roll_no)
print("Subjects:", subjects)
print("Marks:", marks)

topper = max(marks, key=marks.get)
print("Topper:", topper, "-", marks[topper])
