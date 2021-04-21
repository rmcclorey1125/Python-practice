import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]

user_choice = int(input("Choose 0 for rock, 1 for paper or 2 for scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed in an invalid number")
else:
    print(options[user_choice])

    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print(options[comp_choice])

    # print(user_choice)
    # print(comp_choice)
    if user_choice == 0 and comp_choice == 2:
        print("You Win!")
    elif comp_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif comp_choice > user_choice:
        print("You Lose!")
    elif user_choice > comp_choice:
        print("You Win!")
    elif comp_choice == user_choice:
        print("It's a draw")