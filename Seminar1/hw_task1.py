# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#
# Пример:
# 	6 -> да
# 	7 -> да
# 	1 -> нет

a = int(input('Введите номер дня недели: '))

if a > 0 and a <=7:
    if a == 6 or a == 7:
        print('Ура! Это выходной')
    else:
        print('Жаль, это обычный будний день...')
else:
    print('Номер дня недели введен неверно! Попробуйте заново')