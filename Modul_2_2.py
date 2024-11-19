first = input("Введите число first: ")
second = input("введите число second: ")
third = input("введите число third: ")
print(first, second, third)
if first == second == third:
    print('Все равны')
elif first != second and first != third and second != third:
    print('Равных нет')
else:
    print('Равны только 2 числа')