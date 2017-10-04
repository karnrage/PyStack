


def find(list, char): 
    new_list=[]
    for word in list:
        for letter in word:
            if (char == letter):
                new_list.append(word)
                break

    print new_list

word_list = ['hello','world','my','name','is','Anna','root']
char = 'o'

find(word_list, char)

# def whatever(arr,char):
#     new_l = []
#     for word in arr:
#         if char in word:
#             new_l.append(word)
#     return new_l

# print whatever(word_list, chara)
