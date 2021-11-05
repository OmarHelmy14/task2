list1 = [-1, -2, -3, -4, -5, -6]
def sum_of_Odd_and_Even (list2):
    sum_of_Even=0
    sum_of_Odd=0
    for num in list2:
        if num%2 == 0:
            sum_of_Even += num
        else :
            sum_of_Odd +=num 
    return sum_of_Even, sum_of_Odd

print(sum_of_Odd_and_Even(list1))