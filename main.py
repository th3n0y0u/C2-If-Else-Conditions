a = 200
b = 33

if(b > a):
  print("b is greater than a")
else:
  print("b is not greater than a")

# Write a conditional statement that evaluates if the user input is positive or negative
number = input("Please input a number: ")
if (int(number) > 0):
  print(number + " is a positive number.")
elif(int(number) == 0):
  print("You entered 0")
else:
  print(number + " is a negative number")

# Ask the user for their age
# If they are younger than 13, tell them they can only watch PG/G Movies|
# If they are 13 and older but younger than 17, they can only watch PG-13/PG/G movies
# If they are 17 and older, they can watch all movies

age = int(input("Please input your age here: "))
if(age < 13):
  print("You can only watch PG/G rated movies. ")
elif(age < 17):
  print("You can only watch PG-13/PG/G rated movies")
else:
  print("You can watch any movies")

is_Hungry = True
is_Sleepy = False
if(is_Hungry == True):
 print("You should go eat")
elif(is_Sleepy == True):
 print("You should go to sleep")
elif(is_Sleepy == False):
 print("Wow you're well-rested")

# Ask the user for a number
# Tell the user if their number is even or odd
number = input("Please input a number ")
if(int(number) // 2):
 print("Your number is even")
elif(int(number) == 0):
 print("Why do you like 0 always")
else:
 print("Your number is a odd number") 