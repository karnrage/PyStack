class Car(object):
    def __init__(self, price, speed, fuel, miles):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.miles = 0   
    def displayInfo(self):
        print "The cars price is " + str(self.price)
        print "The cars max speed is " + str(self.speed)
        print "The cars odometer reads " + str(self.miles)
        print "The cars MPG reads " + str(self.fuel)
        return self
    def tax(self):
        if self.price > 10000:
            self.price = self.price * 1.15
        else:
            self.price = self.price * 1.12
        return self

chevy = Car(30000, 155, 21, 0)
print chevy.tax().displayInfo()

buick = Car(35000, 125, 31, 0)
print buick.tax().displayInfo()

mazda = Car(36000, 115, 41, 0)
print mazda.tax().displayInfo()

vw = Car(38000, 135, 17, 0)
print vw.tax().displayInfo()

nissan = Car(25000, 145, 27, 0)
print nissan.tax().displayInfo()

plymouth = Car(5000, 90, 26, 0)
print plymouth.tax().displayInfo()