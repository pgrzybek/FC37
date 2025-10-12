import functools
#materialy nie do sprawdzenia poprostu dodatkowa wiedza
class moj_dekorator_klasowy:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)

class PoprawnaImplementacjaDeskryptor:
    @moj_dekorator_klasowy
    def metoda(self):
        print("Metoda zaimplementowana z deskryptorem!")

obiekt = PoprawnaImplementacjaDeskryptor()
obiekt.metoda()
