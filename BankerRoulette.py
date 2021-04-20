import random

names_string = input("Give me everybody's names, seperated by a comma. ")

names = names_string.split(", ")

num_names = len(names)

rand_index = random.randint(0, num_names - 1)

print(names[rand_index])