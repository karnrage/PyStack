class product(object):
    def __init__(self,price,name,weight,brand,cost,status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        if price == 0:
            self.status = "sold"
        if cost == str("return"):
            self.status = "return"
            self.price = 0
        if cost == str ("closed box return"):
            self.status = "like new"
            self.status = "for sale"
        if cost == str ("open box return"):
            self.status = "used"
            self.price = self.price*.8

            


  
    def tax(self, tax):
        self.price = 1+tax * self.price
        print self.price
        return self

    def profit(self):
        self.price = self.cost * 1.2
        print self.profit
        return self
    
        
    # def returned(why):
    #     if why == "defect":
    #         self.status == "defect"
    #         self.price == 0
    #     elif why == "damage":
    #         self.price == self.price * .8
    #     else:
    #         self.status == "for sale"
    #     return self
    def displayInfo(self):
        print "The price is " + str(self.profit)
        print "the name is " + str(self.name)
        print "The weight is " + str(self.weight)
        print "the brand is "+ str(self.brand)
        print "the cost is "+ str(self.cost)
        print self.status
        return self


juice = product(4, "OJ", "64oz", "tropicana",3,"sold" )
print juice.tax(.08).displayInfo()