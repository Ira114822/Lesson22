# entity class
class Human:


    def __init__(self, first_name, surname, age=0, alive=True):
        self._first_name = first_name
        self._surname = surname
        self._age = age
        self._alive = alive

    def __str__(self):
        return f"{self._first_name} {self._surname}:" \
               f"\nage = {self._age}" \
               f"\nis alive = {self._alive}"

    @property
    def firstname(self):
        return self._first_name

    @firstname.setter #декоратор
    def firstname(self, firstname):
        self._first_name = firstname

    @property
    def surname(self):
        return self._surname

    @surname.setter  # декоратор
    def surname(self, surname):
        self._surname = surname

    @property
    def age(self):
        return self._age

    @age.setter  # декоратор
    def age(self, age):
        if age > 0:
            self._age = age

    @property
    def alive(self):
        return self._alive

    @alive.setter  # декоратор
    def alive(self, alive):
        if alive >0:
            self._alive = alive

    @property
    def is_adult(self):
        return self._age >= 18