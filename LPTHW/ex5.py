name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
cmheight = height * 2.54
weight = 180.0 #lbs
kilos = weight * 1.0 / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "Which converts to %d centimeters" % cmheight
print "He's %d pounds heavy." % weight
print "Which converts to %d kilograms" % kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)