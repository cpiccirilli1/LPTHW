#Brings in argv from sys package
from sys import argv
#unpacks argv and assigns variables
script, filename = argv
# Printing
print "We're going to erase %r." % filename
print "IF you don't want that hit CTRL-C (^C)"
print "If you do want that, hit RETURN."
#Chance to cancel using terminal escape command
raw_input("?")
#printing and assigns  the open file
print "Opening the file..."
target = open(filename, 'w')
#truncates the target file by using .truncate module
print "Truncating the file. Goodbye!"
target.truncate()
# printing and assigning variables to strings
print "now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#printing and writing the above variables using formmating and escapes.
print "I'm going to write these to the file."
target.write("\n %s \n %s \n %s" % (line1, line2, line3))
# closes the file
print "Now to close the file..."
target.close()
print "File closed!"