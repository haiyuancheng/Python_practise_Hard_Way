#Variable and Names

cars =  100 # variable cars are 100

space_in_a_car = 4.0
#space_in_a_car = 4
drivers = 30

passengers =  90

cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capaciry = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars are available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
print "Hey %s there." % "you" #%s show variable way

#What is the difference between = (single-equal) and == (double-equal)?
#The = (single-equal) assigns the value on the right to a variable on the left.
# The == (double-equal) tests if two things have the same value. You'll learn about this in Exercise 27