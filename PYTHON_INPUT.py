from sys import argv
script, num = argv #Script name is first command line argument

prompt = ">>"

print("Fav color? ")
color = input(prompt)

print(f"You will need to input {num} numbers")

print("Age? ", end='') #do not end the line
age = int(input())

name = input("What is your name? ")

