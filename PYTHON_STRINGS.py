#Print statements
name = 'Zero'
print(f"My name is {name}")
print("My name is " + name)
print("My name is",name,", not Jacayla") # Unneccesary space before and after formatted variable

print("Is 2 greater than 5?", 2 > 5)

#Formatting a variable
color = f"My favorite color has nothing to do with my name, {name}"
print(color)

funny = True
joke_eval = "I am so funny right? {}"
print(joke_eval.format('No girl'))
print("No, but your mom is {}".format("cute"))

end1 = 'Z'
end2 = "E"
end3 = 'R'
end4 = 'O'
print(end1 + end2 + end3 + end4, end='\n')


theformat = "{} {} {}"
print(theformat.format("Zero", "Is", "Cool"))
print(theformat.format(theformat, theformat, theformat))

print("""Use three double-quotes 
in order to type alot like so""")

print("\tThis a tab")
print("This sentence is split\non a line")
print("You have to do this \\ to get it.")




