numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,
           345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
           687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831,
           445, 742, 717, 958,743, 527]
cnt = len(numbers)
print(f'Количество номеров в исходном списке: {cnt}')
even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    elif i == 815:
        break

print(f'Четные номера из списка, расположенные левее числа 815 : {even_numbers}')
print(f'Количество отсортированных чисел: {len(even_numbers)}')


#even_numbers = [i for i in numbers if i % 2 == 0 and i <= 815 elif i == 815]
#print(even_numbers)