import random
#random_toss=[]

def tosses():
    print "Starting the program..."
    t_head = 0
    t_tail = 0

    for toss in range(0,5001):
        random_toss = random.randint(0, 1)
        print ("Attempt #"+ str(toss))       
        if (random_toss == 1):
            t_head = t_head + 1
            print (t_head, "heads")
        else:
            t_tail = t_tail +1
            print (t_tail, "tails")

tosses()