def odd_even():
    for num in range (0,2001):
        if (num%2==1):
            print "Number is",num,". This is an odd number."
        else:
            print "Number is",num,". This is an even number."

odd_even()

def multiply(arr, num): #name parameters and internal variables differnt names
    new_list = []
    # print new_list
    for val in arr:
        # print num
        
        new_list.append(val * num)
    print new_list
    # print arr
    return new_list
    
        

a = [2,4,10,16]
b = multiply(a, 5)
print b

def challengee(arr):
    new_array=[]
    for val in arr:
        temp = []
        for x in range(val):
            temp.append(1)

        new_array.append(temp)
    return new_array
x = challengee(multiply([2,4,5],3))
print x

