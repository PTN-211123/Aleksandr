plus_task = input('Введите пример со сложением: ')
nums_list = plus_task.split(' + ')
res = 0
for i in nums_list:
    res += int(i)
print(f'Результат: {res}')

