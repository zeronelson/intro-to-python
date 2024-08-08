from sys import argv
from os.path import exists

script, filename, destfile = argv

in_data = open(filename).read() # CONTENTS OF FILE NAME SAVED TO INDATA
fromfile = open(destfile, 'w')
fromfile.write(in_data)


#Reads file
txt = open(filename) #returns file object 

print(f"Contents of {filename}: ")
print(txt.read()) #read file content

txt.close()

#Writes to file and then reads it
txt = open(filename, 'w+') #Opening file with write and read permissions
txt.truncate() #Erases entire file
txt.write("I love you and you're not cute.")
txt.read()
txt.close()

