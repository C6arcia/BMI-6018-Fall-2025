#Write a python program that, given an input list, will filter the input above a user defined threshold. 
#This is to be done with a standard function.
#That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]

input_list = [1,2,3,4,5,6,7,8,9]
defined_threshold = 6
def function_filter_list(input_list, defined_threshold):
    filtered = []
    for item in input_list:
        if item <= defined_threshold:
            filtered.append(item)
    return filtered
result = function_filter_list(input_list, defined_threshold)
print(result)
