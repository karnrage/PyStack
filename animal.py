class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def walk(self):
        self.health += 1
        return self
        # print self
    def run(self):
        self.health += 5
        return self
        # print self
    def display(self):
        print "the health is " + str(self.health)
        print "the animal is " + self.name

stripes = animal("zebra", 100)
print stripes.walk().walk().walk().run().run().display()

class dog(object):
    def animal(self):
    self.health = 150
    
