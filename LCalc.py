print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
lower_case_names = names.lower()
t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")

true = t + r + u + e

l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")

love =  + l + o + v + e

score = str(true) + str(love)

if int(score) < 10 or int(score) > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
  print(f"Your score is {score} you are alright together.")
else:
  print(f"Your score is {score}")
