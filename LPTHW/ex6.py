# This uses modulous d as a place holder for the actual integer
x = "There are %d types of people." % 10
# creates the variable binary and assigns it "binary"
binary = "binary"
# creates the variable do_not and assigns it the string "don't"
do_not = "don't"
# creates the variable y and assigns it a string with 2 modulous replacement symbols.
y = "Those who know %s and those who %s" % (binary, do_not)
#prints variable x
print x
# prints variable y
print y
#prinst a string and replaces the modulous symbol with another string.
print "I said: %r." % x
print "I also said: %s." % y

# assigns the variable hilarious the boolean value of False
hilarious = False
#Assigns the variable a string with a modulous r symbol embedded
joke_evaluation = "Isn't that joke so funny?! %r"
# prints joke_evaluation and fills the modulous with the boolean assigned to hilarious
print joke_evaluation % hilarious
# assigns the variables w and e strings
w = "This is the left side of ..."
e = "a strinkg with a right side."
# prints the strings w and e run together
print w + e