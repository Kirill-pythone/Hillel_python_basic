my_str = [1, 3, 2, 4, 1, 23, 4, 2, 3, 5]
my_str1 = []
count_symbol = 0
for i in my_str:
    if my_str.count(i) == 1:
        my_str1.append(i)

print(my_str1)


