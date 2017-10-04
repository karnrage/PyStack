# words = "It's thanksgiving day. It's my birthday,too!"
# catch = "day"
# temp = [(words.find(i), i) for i in catch if i in words]
# print temp
# print min(temp)[1]

#find & replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.index("day")
words.replace("day", "month")
print words

#min & max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1] 

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()

#len(x)

first_half=x[:len(x)/2]
second_half=x[len(x)/2:]
print first_half, second_half
second_half.insert(0,first_half)
print second_half