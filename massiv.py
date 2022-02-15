from random import randint

number = int(input("Enter first number-> "))
list = []
print(f"Calc: additt = ", number+number)
print(f"Calc: subt = ", number-number)
print(f"Calc: Mult = ", number*number)
print(f"Calc: Divis = ", number/number)
for i in range(number):
    list.append(randint(-100, 100))
print(list)
