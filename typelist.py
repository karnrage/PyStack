#assignment:type list

def type_list(l):
    new_string = "" 
    sum = 0
    for i in (l):
        if isinstance (i,str): #MUST place "if" in front of "isinstance" for computer to keep, and to move on with evaluated value, otherwise value is lost
            new_string = new_string +" "+ i
            
        elif (isinstance (i,int)) or (isinstance (i, float)) : 
             sum = sum + i
             
        else:
            print "broke"
            break
    print new_string
    print sum

l = ['magical','unicorns']
m = [2,3,1,7,4,12]
n = ['magical unicorns',19,'hello',98.98,'world']

type_list(n)
