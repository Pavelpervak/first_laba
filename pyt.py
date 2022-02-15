from random import randint

print("Hello in my calculator and array generator!")
running = True
list = []


def summ(a, b):
    print(f" a + b = ", a+b)


def subt(a, b):
    print(f" a - b = ", a-b)


def mult(a, b):
    print(f" a * b = ", a*b)


def divis(a, b):
    print(f" a / b = ", a/b)


def massiv():
    quaantity = int(input("Number of numbers generated-> "))
    for i in range(quaantity):
        list.append(randint(-100, 100))
    print(list)
    list.clear()


while running:
    message = input(
        "Click 't' for calculator, 'p' for array generator, 'q' for exit: ")
    if message == 'q':
        running = False
        print("Thanks for using!")
    elif message == 'p':
        massiv()
    elif message == 't':
        mes = input(
            "Click '+' for Addition, '-' for Subtraction, '*' for Multiplication, '/' for Division: ")
        first = float(int(input("First number -> ")))
        second = float(int(input("Second number -> ")))
        if mes == '+':
            summ(first, second)
        elif mes == '-':
            subt(first, second)
        elif mes == '*':
            mult(first, second)
        elif mes == '/':
            divis(first, second)
    else:
        print("Please, try again!")
