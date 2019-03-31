# Imports sys and os.path
from sys import argv
from os.path import exists
# unpacks argv
script, from_file, to_file = argv

#we could do these two on one line too, how?
indata = open(from_file).read()
#creates in_file and opens the cpy file
#indata is created and reads the contents of the cpy file

# counts the number of bytes, prints
print "The input file is %d bytes long" % len(indata)
#checks if output exists
print "Does the output file exist? %r" % exists(to_file)
# creates variable and opens/pastes txt from cpy file in the paste file
out_file = open(to_file, 'w')
out_file.write(indata)
# prints
print "Alright, all done."
#closes both files.
out_file.close()
