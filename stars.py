
# def draw_stars(arr):
    
#     for val in arr:
#         stringg = "" #put string inside of loop to reset back to empty
#         # temp = []
#         for x in range(val):
#             # print val # proved that string was adding newer values without clearing old string value. showed that string needed to be moved inside of loop
#             # temp.append("*")
#             stringg += "* "
#         print stringg
#         # new_array.append(temp)
#     # return new_array
            

# x = [4, 6, 1, 3, 5, 7, 25]
# print draw_stars(x)


def draw_stars(arr):
    
    for val in arr:
        if isinstance(val, int):
            stringg = "" #put string inside of loop to reset back to empty
            # temp = []
            for x in range(val):
                # print val # proved that string was adding newer values without clearing old string value. showed that string needed to be moved inside of loop
                # temp.append("*")
                stringg += "* "
            print stringg
            # new_array.append(temp)
        else:
            char = ""
            for x in range(0,len(val)): ## grab first letter, multipy into string 
                val[0]
                char += val[0]
            print char
            # print val.lower()
            # print len(val)


        # return new_array
            

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

print draw_stars(x)