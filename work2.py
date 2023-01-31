# Найти сумму цифр в вещественном числе 
n = str(input("Введите вещественное число:\n"))
lst = list(map(int, [i for i in n if i.isdigit()]))
sum = 0
for i in lst:
    sum+=i
print(f'Сумма чисел в вещественном числе = {sum}')