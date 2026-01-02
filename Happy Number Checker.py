from functools import reduce

def happy_number(a):
    str_a = a.replace('', ' ').split()
    int_a = list(map(int, str_a))
    sum_list = reduce(lambda a,b : a**2 +b**2, int_a)
    happy_num_found = False
    if sum_list == 1:
        return f"Happy Number, Final Sum = {sum_list}"
    elif type(sum_list) == float or type(sum_list) == str:
        return f"Not a Happy Number, Final Sum = {sum_list}"
    elif type(sum_list) == int and sum_list != 1:
        while False:
            str_sumlist = str(sum_list).replace('',' ').split()
            int_sumlist = list(map(int, str_sumlist))
            sum_list = reduce(lambda a,b : a**2 +b**2, int_sumlist)
            int_sumlist = []
            if sum_list == 1:
                return f"Happy Number, Final Sum = {sum_list}"
                True
            else:
                False
    elif happy_num_found == True:
        return f"Happy Number, Final Sum = {sum_list}"
    else:
        return f"Not a Happy Number, Final Sum = {sum_list}"
user = input("Enter Number: ")
print(happy_number(user))
  
