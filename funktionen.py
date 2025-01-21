# funktionen.py
def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b

def subtrahiere(a, b):
    """Subtrahiert zwei Zahlen."""
    return a - b

def multipliziere(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b

def dividiere(a, b):
    """Dividiert zwei Zahlen. Wirft einen Fehler bei Division durch null."""
    if b == 0:
        raise ZeroDivisionError("Division durch Null ist nicht erlaubt.")
    return a / b