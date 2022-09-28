# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
# сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

try:
    file, time, stavka, bonus = sys.argv
except ValueError:
    print("Value Error")
    exit()

def salary(time, stavka, bonus):
    salary = time * stavka + bonus
    return salary

print(salary(int(time), int(stavka), int(bonus)))
print(file)
