user_num = int(input('Введите число: '))
num_list = []
num_sum = 0
for i in range(user_num):
    num_list.append(i + 1)
    num_sum += i + 1
#num_list = [(i + 1) + for i in range(user_num)]

print(f'Список чисел в диапазоне от 1 до {user_num}: {num_list}')
print(f'Сумма чисел списка равна: {num_sum}')
