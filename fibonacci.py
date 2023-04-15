# Программа для вычисления n-го числа Фибоначчи

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Введите номер числа Фибоначчи: "))

print("Число Фибоначчи под номером", num, "равно", fibonacci(num))
