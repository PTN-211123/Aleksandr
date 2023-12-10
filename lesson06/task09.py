sum1 = 0
even_list = [i for i in range(100) if i % 2 == 0]
for i in even_list:
    sum1 += i
sum2 = 0
odd_list = [i for i in range(100) if i % 2]
for i in odd_list:
    sum2 += i
print(f'Список четных чисел: {even_list}')
print(f'Сумма четных чисел: {sum1}')
print(f'Список нечетных чисел: {odd_list}')
print(f'Сумма нечетных чисел: {sum2}')