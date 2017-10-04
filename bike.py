class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed   
    def displayInfo(self):
        print "The bikes price is " + str(self.price)
        print "The bikes max speed is " + str(self.max_speed)
        print "The bikes odometer reads " + str(self.miles)
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 10
        return self


bike1 = Bike(300, 100, 5)
print bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(200, 150, 50)
print bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(500,200,100)
print bike3.reverse().reverse().reverse().displayInfo()

