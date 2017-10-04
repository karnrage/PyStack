import random

def scores():
    print "Scores and Grades"
    random_num = random.randint(60, 100)
    print random_num
    if (60 <= random_num and random_num <= 69):
        print "Score:",random_num,"; Your grade is D"
    elif (70 <= random_num and random_num <= 79):
        print "Score:",random_num,"; Your grade is C"
    elif (80 <= random_num and random_num <= 89):
        print "Score:",random_num,"; Your grade is B"
    else: #(90 <= random_num and random_num <= 100):
        print "Score:",random_num,"; Your grade is A"
print "End of the prgoram. Bye!"

scores()