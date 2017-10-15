call_List=[]
class call(object):
    def __init__(self, unique_id, caller_name, caller_number, time_called, reason_called):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_called = time_called
        self.reason_called = reason_called

    def display(self):
        print "This callers unique id is " + str(self.unique_id)
        print "This callers name is " + self.caller_name
        print "The caller ID says the number from which this call is coming in from is "+ str(self.caller_number)
        print str(self.time_called)+" is when the caller called"
        print self.reason_called+" is why the caller called"
        return

class call_center(object):
    def __init__(self, calls, queue):
        self.calls = []
        self.queue = len(queue)
        return
    def add(self, unique_id, caller_name, caller_number, time_called, reason_called): #creating/adding new caller to list, in order to use the previous classes method, the previous classes parameters need to be taken in, in order to pass them to the previous classes method in order to satisify its parameter list
        call(caller_name, unique_id,caller_number, time_called, reason_called)
        return
    def remove(self):
        del self.calls [0]
    def displayInfo(self):
        for bitching in self.list:
            print "The name of the caller is"+ bitching.caller_name +" and their phone number is"+ str(bitching.caller_number)
        print "The quantity of todays calls is" +str(len(call_List))

# xx = call(545,"kam", 6302793555,1700,"broke_internet")
# print xx.display()

x2 = call_center()
call_center().add("The rock", 6303339504, 1300 )
        

        

        

        







# class call_center(object):