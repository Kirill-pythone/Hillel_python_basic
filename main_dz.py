my_results1 = ['Hello', 'hi', 'bread', 1, 2, 3, 5, 2, 7, 45, 7]
my_results2 = [2, 1, 4, 53, 6, 4]
my_results = []
for i in my_results1[2::2]:
    my_results.append(i)

for w in my_results2[1::2]:
    my_results.append(w)

print(my_results)
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [6, 7, 8, 9, 10]
#
#
# even_elements_1 = [my_list_1[i] for i in range(len(my_list_1)) if i % 2 == 0]
#
#
# odd_elements_2 = [my_list_2[i] for i in range(len(my_list_2)) if i % 2 != 0]
#
#
# my_result = even_elements_1 + odd_elements_2
#
# print(my_result)
