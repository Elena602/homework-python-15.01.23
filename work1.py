# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [27, 13, 5, 95, 3, 52, 9]
print(sum(list(filter(lambda i: i%2, list))))