#number of cars
cars=100
#How many people the cars can hold
space_in_a_car = 4
#how many are driving people are available
drivers = 30
#how many passengers need rides
passengers = 90
#number of cars not being driven because their isn't enough drivers
cars_not_driven = cars - drivers
#Number of cars driven = drivers available
cars_driven = drivers
#Number of people able to fit in all the cars
carpool_capacity = cars_driven*space_in_a_car
#Finds out how many people need to go in each car being driven
average_passengers_per_car = passengers/cars_driven


print "There are" , cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."

#carpool_capacity was not an existing variable and therefore
#could not be called. 

