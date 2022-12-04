class1 = int(input('Введите количество учеников  в 1 классе :'))
class2 = int(input('Введите количество учеников  в 2 классе :'))
class3 = int(input('Введите количество учеников  в 3 классе :'))
result1 = (class1 // 2)
result1_1 = (class1 % 2)
result2 = (class2 // 2)
result2_2 = (class2 % 2)
result3 = (class3 // 2)
result3_3 = (class3 % 2)
result_123 = result1 + result2 + result3
result1_2_3 = result1_1 + result2_2 + result3_3
print('Столько парт всего нужно закупить25')
print(result_123+result1_2_3)
