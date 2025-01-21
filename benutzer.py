# benutzer.py
class Benutzer:
    def __init__(self, name, alter):
        if not isinstance(name, str):
            raise TypeError("Der Name muss ein String sein.")
        if not isinstance(alter, int) or alter < 0:
            raise ValueError("Das Alter muss eine positive Ganzzahl sein.")
        self.name = name
        self.alter = alter