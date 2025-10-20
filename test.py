import unittest

def textNaVelkaPismena(text):
    return text.upper()

class TestTextNaVelkePismena(unittest.TestCase):

    def test_prevod_slova(self):
        self.assertEqual(textNaVelkaPismena("abc"), "ABC")
    
    def prevod_vety(self):
        self.assertEqual(textNaVelkaPismena("a b c"), "A B C")
    
    def prevod_cisel(self):
        self.assertEqual(textNaVelkaPismena("123"), "")

    def prazdny_vstup(self):
        self.assertEqual(textNaVelkaPismena("", ""))


if __name__ == "__main__":
    unittest.main()