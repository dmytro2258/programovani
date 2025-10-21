import unittest

class Hrac:
    def __init__(self, vek, jmeno="Honza"):
        self.__vek = vek
        self.__jmeno = jmeno

    def get_vek(self):
        return self.vek

    def set_vek(self, vek):
        self.__vek = vek

    def get_jmeno(self):
        return self.__jmeno

    def set_jmeno(self, jmeno):
        self.__jmeno = jmeno

class TestHrac(unittest.TestCase):
    
    def test_vytvoreni(self):
        hrac = Hrac(10)
        self.assertEqual(hrac.get_jmeno(), "Honza")


if __name__ == "__main__":
    unittest.main()


"""Otestujte vytvoření objektu Hrac s výchozím jménem.
Otestujte vytvoření objektu Hrac se zadaným jménem.
Otestujte správné nastavení a získání věku.
Otestujte správné nastavení a získání jména."""