# taschenrechner.py
class Taschenrechner:
    def addiere(self, a, b):
        return a + b

    def subtrahiere(self, a, b):
        return a - b

    def multipliziere(self, a, b):
        return a * b

    def dividiere(self, a, b):
         if b == 0:
            raise ZeroDivisionError("Division durch Null ist nicht erlaubt.")
         return a / b