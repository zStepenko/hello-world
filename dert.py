#линейные алгоритмы

#пример 1
#форматированный вывод (2 способа)
'''
import math
x = float(input('x = '))
print('sin(%.2f) = %.2f' % (x, math.sin(x)))
print('sin({0:.2f}) = {1:.2f}'.format(x, math.sin(x)))
'''

#пример 2
#вычисляем количество десятков числа (2 цифру)
#операции // и %
'''
y = int(input('Введите трехзначное число: '))
print('Количество десятков равно ', (y // 10) % 10)
'''

#пример 3
#вывод в одну строку
'''
z = input('z = ')
print('Вы ввели ', end='')
print(z)
'''

#задание 1
'''
a, b = input('Введите число A: '), input('Введите число B: ')
print('A = ',a,'B = ',b)
a, b = b, a
print(a,b)
'''

#задание 2
'''
s = input('Введите число: ')
print(s,',', int(s),',', float(s))
print()
print(type(s), s)
print(type(int(s)), int(s))
print(type(float(s)), float(s))
'''

#задание 3
'''
a = int(input('Введите трехзначное число: '))
print('Сумма цифр данного трехзначного числа равна ', (a % 10 + (a // 10) % 10 + a // 100))
'''

#задание 4
'''
print('Перевернутое число: ',input()[::-1])
'''

#задание 5
'''
x1, x2 = float(input('Введите x1: ')), float(input('Введите x2: '))
y1, y2 = float(input('Введите y1: ')), float(input('Введите y2: '))
print('Расстояние между двумя точками равно ',(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5))
'''

#задание 6
'''
x1, y1 = float(input('Введите x1: ')), float(input('Введите y1: '))
x2, y2 = float(input('Введите x2: ')), float(input('Введите y2: '))
x3, y3 = float(input('Введите x3: ')), float(input('Введите y3: '))
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
p = (a + b + c)/2
print('Периметр треугольника равен ', round(p*2, 2))
print('Площадь треугольника равна ',round(((p * (p - a) * (p - b) * (p - c)) ** 0.5), 2))
print('Площадь треугольника равна ',round((abs(((x1 - x3) * (y2 - y3)) - ((x2 - x3) * (y1 - y3)))/2),2))
'''

#задание 7
'''
p1, p2 = float(input('Введите цену p1: ')), float(input('Введите цену p2: '))
p3, p0 = float(input('Введите цену p3: ')), float(input('Введите цену p0: '))
pr1 = (p0 + p1)/3
pr2 = pr1 + (p2 - p1)/2
pr3 = pr2 + (p3 - p2)
print('Первый пассажир заплатил',round(pr1,2),'р.')
print('Второй пассажир заплатил',round(pr2,2),'р.')
print('Третий пассажир заплатил',round(pr3,2),'р.')
'''

#задание 8
'''
a = float(input('Введите первый корень: '))
b = float(input('Введите второй корень: '))
c = float(input('Введите третий корень: '))
print('Кубическое уравнение имеет вид:')
print('(x-(',a,'))','(x-(',b,'))','(x-(',c,'))',sep='')
print('ИЛИ')
print('x^3+(',-1*round((a+b+c),1),')*x^2+(',round((a*b+b*c+a*c),1),')*x+(',round((-a*b*c),1),')',sep='')
'''

#условный оператор

#пример 1
'''
x = int(input('Введите x:'))
if x > 0:
    print('x>0')
else:
    print('x<=0')
'''

#пример 2
'''
if x < 0:
    x = - x
print('|x|=',x)
#другой вариант if
if x < 0: x = -x
print('|x|=',x)
'''

#пример 3
#решаем уравнение A*x+B=0
'''
A = float(input('A = '))
B = float(input('B = '))
if A == 0:
    if B == 0:
        print('x - любое число')
    else:
        print('нет решения')
else:
    print('x = {0:.2f}'.format(-B/A))
'''

#пример 4
#определяем время года по номеру месяца
'''
m = int(input('Введите номер месяца: '))
if m > 2 and m < 6:
    print('весна')
elif 6 <= m <= 8:
    print('лето')
elif 9 <= m <= 11:
    print('oсень')
elif m == 12 or m == 1 or m == 2:
    print('зима')
else:
    print('введите правильно номер месяца')
'''

#задание 1
'''
a = float(input('Введите левую границу диапазона: '))
b = float(input('Введите правую границу диапазона: '))
x = float(input('Введите значение: '))
if a <= x <= b:
    print('Yes')
else:
    print('No')
'''

#задание 2
'''
y = int(input('Введите номер года: '))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('Високосный')
else:
    print('Не високосный')
'''

#задание 3
'''
b = int(input('Введите вашу оценку: '))
if b > 85:
    print('Отлично!')
elif 70 <= b <= 85:
    print('Хорошо!')
elif 50 <= b < 70:
    print('Удовлетворительно!')
else:
    print('Пересдача!')
'''

#задание 4
'''
a = int(input('Введите левую границу первого отрезка: '))
b = int(input('Введите правую границу первого отрезка: '))
c = int(input('Введите левую границу второго отрезка: '))
d = int(input('Введите правую границу второго отрезка: '))
res = set(set([int(i) for i in range(a, b+1)]) & set([int(j) for j in range(c, d+1)]))
if len(res) > 0:
    print('Пересечение отрезков [a,b] и [c,d] есть отрезок [',min(list(res)),',',max(list(res)),']',sep='')
else:
    print('Отрезки не пересекаются!')
'''

#задание 5
'''
a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))
if a == 0:
    if b == 0:
        if c == 0:
            print('Решение - любое число')
        else:
            print('Нет решений!')
    else:
        print('x = {0:.2f}'.format(-c / b))
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Нет решений!')
    elif d == 0:
        print('x = {0:.2f}'.format(-b/2*a))
    else:
        print('x1 = {0:.2f}'.format((-b-d**0.5)/2*a))
        print('x2 = {0:.2f}'.format((-b+d**0.5)/2*a))
'''

#задание 6
'''
a, b, c, d = int(input('a = ')), int(input('b = ')), int(input('c = ')), int(input('d = '))
min1 = a
if min1 > b:
    min1 = b
min2 = c
if min2 > d:
    min2 = d
min = 0
if min1 < min2:
    min = min1
else:
    min = min2
print(min)
'''

#задание 7
'''
a, b, c = int(input('a = ')), int(input('b = ')), int(input('c = '))
if (a + b > c) and (b + c > a) and (a + c > b):
    r = [a,b,c]
    if min(r) ** 2 + (sum(r)-max(r)-min(r)) ** 2 == max(r) ** 2:
        print('Можно составить прямоугольный треугольник!')
    else:
        print('Можно составить непрямогуольный треугольник!')
else:
    print('Нельзя составить треугольник!')
'''

#задание 8
'''
x, y, z = float(input('x = ')), float(input('y = ')), float(input('z = '))
st1 = (x >= 0) and (x == int(x))
st2 = (y >= 0) and (y == int(y))
st3 = (z >= 0) and (z == int(z))
if (st1 and st2) and not(st2 and st3) and not(st1 and st3):
    print('F = 1')
elif not(st1 and st2) and (st2 and st3) and not(st1 and st3):
    print('F = 1')
elif not(st1 and st2) and not(st2 and st3) and (st1 and st3):
    print('F = 1')
else:
    print('F = 0')
'''

#задание 9
'''
print('Введите координаты точки: ')
x,y = float(input('x = ')), float(input('y = '))
if x >= 0 and y >= 0:
    print('F = 1')
elif x < 0 and y >= 0:
    print('F = 2')
elif x < 0 and y < 0:
    print('F = 3')
else:
    print('F = 4')
'''

#задание 10
'''
if input().find('7') == -1:
    print('F = 0')
else:
    print('F = 1')
'''

#задание 11
'''
x1, x2, x3, x4 = float(input('x1 = ')), float(input('x2 = ')), float(input('x3 = ')), float(input('x4 = '))
if x1 == x4:
    if x1 == x2:
        f = x3
        n = 3
    else:
        f = x2
        n = 2
else:
    if x1 == x2:
        f = x4
        n = 4
    else:
        f = x1
        n = 1
print('Число',f,'с номером',n)
'''

#задание 12
'''
n = int(input('Введите число: '))
if (n%100 == 11) or (n%100 == 12) or (n%100 == 13) or (n%100 == 14):
    print(n,'рублей')
else:
    if (n%10 == 1):
        print(n,'рубль')
    elif (n%10 == 2) or (n%10 == 3) or (n%10 == 4):
        print(n,'рубля')
    else:
        print(n,'рублей')
'''





