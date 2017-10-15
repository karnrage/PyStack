#part 1 completed
class mathDojo(object):
    def __init__(self):
        self.sum = 0
        
    def add (self, *x):
        for i in range(len(x)):
            self.sum += x[i] 
        return self
            # print "got "+arg1+" and "+ ",".join(args)
    def sub (self, *y):
        for i in range(len(y)):
            self.sum -= y[i]
        return self

    def displayInfo(self):
        print self.sum          


md = mathDojo()
md.add(2).add(2,5).sub(3,2).displayInfo()

#part 2 starts here