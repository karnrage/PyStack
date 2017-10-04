#multipes part 1. Prints all odds up to 1001. if remainder after division, means it is odd and will print
for count in range(0,1001):
    if count%2==1:
        print count
#multipes part 2. Prints all #'s divisible by 5. if no remainder after division by 5, then will print
for count in range(5,1000001):
    if count%5==0:
        print count
#sum list. define a variable to hold the sum, go through the list and total the values. return sum 
def list_sum(yz):
    myysum = 0
    # print "here"
    for count in yz:
        myysum = count + myysum
        # print myysum
    return myysum

a = [1, 2, 5, 10, 255, 3]

print list_sum(a)
#avg list. same as above except adding a divisor of total items to get the avg.
def list_avg(z):
    myysum = 0
    # print "here"
    for count in z:
        myysum = count + myysum
        # print myysum
        avgg = myysum/len(a)
    return avgg

a = [1, 2, 5, 10, 255, 3]

print list_avg(a)