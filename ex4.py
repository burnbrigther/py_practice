cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
# cars_not_driven is assigned the static value of cars (100) - drivers (30)
cars_not_driven = cars - drivers
# cars_driven is being assigned the value of drivers
cars_driven = drivers
# carpool_capacity is being assigned the value of cars_driven multiplied by the value of space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# Initialize a variable called average_passengers_per_car and compute passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven
 
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."