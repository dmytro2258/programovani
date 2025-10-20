import unittest

class Teplomer:
    def __init__(self, max_teplota=100):
        """Inicializuje objekt teploměru s výchozí teplotou 0 a maximální teplotou."""
        self.teplota = 0
        self.max_teplota = max_teplota

    def nastav_teplotu(self, nova_teplota):
        """Nastaví aktuální teplotu na hodnotu nova_teplota.
        Pokud přesáhne maximální teplotu, vyvolá výjimku."""
        if nova_teplota > self.max_teplota:
            raise ValueError("Teplota přesáhla maximální povolenou hodnotu!")
        self.teplota = nova_teplota

    def oteplit(self, stupne):
        """Zvýší teplotu o zadaný počet stupňů.
        Pokud výsledná teplota přesáhne maximální povolenou hodnotu, vyvolá výjimku."""
        if self.teplota + stupne > self.max_teplota:
            raise ValueError("Teplota přesáhla maximální povolenou hodnotu!")
        self.teplota += stupne

    def ochladit(self, stupne):
        """Sníží teplotu o zadaný počet stupňů.
        Teplota nesmí klesnout pod -273.15 °C."""
        nova_teplota = self.teplota - stupne
        self.teplota = max(nova_teplota, -273.15)



class TestTeplomer(unittest.TestCase):
    def test_inicializace(self):
        teplomer = Teplomer()
        self.assertEqual(teplomer.teplota, 0)
        self.assertEqual(teplomer.max_teplota, 100)
        
    def test_nastaveni_teploty(self):
        teplomer = Teplomer()
        teplomer.nastav_teplotu(50)
        self.assertEqual(teplomer.teplota, 50)
        self.assertRaises(ValueError, teplomer.nastav_teplotu, 150)
        
    def test_zvyseni_teploty(self):
        teplomer = Teplomer()
        teplomer.oteplit(50)
        self.assertEqual(teplomer.teplota, 50)
        teplomer.oteplit(50)
        self.assertEqual(teplomer.teplota, 100)
        self.assertRaises(ValueError, teplomer.oteplit, 150)
        
    def test_snizeni_teploty(self):
        teplomer = Teplomer()
        teplomer.ochladit(100)
        self.assertEqual(teplomer.teplota, -100)
        teplomer.ochladit(200)
        self.assertEqual(teplomer.teplota, -273.15)
        
    

if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
    
    

"""
* 1 **Test inicializace:**

Ověřte, že se teplota správně inicializuje na 0 a maximální teplota na zadanou hodnotu (výchozí je 100).

* 2 **Test nastavení teploty:**

Nastavte teplotu na hodnotu v povoleném rozmezí a ověřte, že se hodnota nastavila správně.
Zkontrolujte, že pokus nastavit teplotu nad limit vyvolá ValueError.

* 3 **Test zvýšení teploty:**

Ověřte, že zvýšení teploty v rámci povoleného rozmezí proběhne správně.
Zkontrolujte, že zvýšení teploty nad limit vyvolá ValueError.

* 4 **Test snížení teploty:**

Ověřte, že snížení teploty proběhne správně a nedostane se pod -273.15 °C.
Pokud je požadavek snížení pod -273.15 °C, ověřte, že se teplota nastaví na -273.15 °C a ne méně.
"""