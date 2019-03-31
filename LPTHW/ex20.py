#imports argv from sys
from sys import argv
# argv variable names
script, input_file = argv
# function to read a file
def print_all(f):
	print f.read()
#function to rewind file using .seek(0)
def rewind(f):
	f.seek(0)
#prints a line and the line number. Uses 
# .readline() to read the actual line
def print_a_line(line_count, f):
	print line_count, f.readline()
#opens the file to be read
current_file = open(input_file)
# prints prompt
print "First let's print the whole file:\n"
#passes open file to print_all
print_all(current_file)
# prints a prompt. Rewinds to the very beginning of document
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"
#sets current line, and then reads the line at that count.
current_line = 1
print_a_line(current_line, current_file)
# modifies current line by adding one. This probably could be done with a loop command.
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)