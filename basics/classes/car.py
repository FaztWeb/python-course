class Car:
    """Abstraction of the Object Car"""
    def __init__(self, gasoline):
        self.gasoline = gasoline
        print "We have ", gasoline, "liters"

    def tear(self):
        if self.gasoline > 0:
            print "Starts"
        else:
            print "Doesn't Start"

    def drive(self):
        if self.gasoline > 0:
            self.gasoline -= 1
            print self.gasoline, " liters left"
        else:
            print "it does not move"

my_car = Car(3)

print type(my_car) #instance
print my_car.gasoline
print my_car.tear()

print my_car.drive()
print my_car.drive()
print my_car.drive()
print my_car.drive()

print my_car.tear()
