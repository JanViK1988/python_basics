"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByNull:
    def __init__(self, divider, denomin):
        self.divider = divider
        self.denomin = denomin

    @staticmethod
    def divide_by_null(divider, denomin):
        try:
            return (divider / denomin)
        except:
            return (f"Делить на ноль нельзя")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 2.2))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))