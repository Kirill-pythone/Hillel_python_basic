b = int(input('Введите первое число:'))
a = int(input('Введите второе число:'))
r = int(input('Виберите операцию \n+-1 \n--2 \n*-3 \n/-4 \n**-5 \n :'))
if r == 1:
    print(b + a)
elif r == 2:
    print(b - a)
elif r==3:
    print(b*a)
elif r==4:
    print(b/a)
elif r==5:
    print(b**a)

