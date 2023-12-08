#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# less_equal_5_list = []
# more_5_list = []
# for i in a:
#     if i <= 5:
#         less_equal_5_list.append(i)
#     elif i > 5:
#         more_5_list.append(i)
# print(f'Список чисел меньше или равных 5: {less_equal_5_list}')
# print(f'Список чисел больше 5: {more_5_list}')

#############################################################
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_equal_5_list = [i for i in a if i <= 5]
more_5_list = [i for i in a if i > 5]
print(f'Список чисел меньше или равных 5: {less_equal_5_list}')
print(f'Список чисел больше 5: {more_5_list}')