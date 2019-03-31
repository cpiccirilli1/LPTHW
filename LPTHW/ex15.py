# imports module argv from sys
from sys import argv

# script and filename are passed the variables
# set on the command line.
script, filename = argv
#txt is created and assigned to open a filename
# assigned to the variable file name
txt = open(filename)
# tells you the file name and then prints 
# the text of the file
print "Here's your file %r:" % filename
print txt.read()
txt.close()
# Asks for the file name again so it can read
# the contents once again.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()