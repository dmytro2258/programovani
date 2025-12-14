import logging
import unittest

logger = logging.getLogger("kino_system")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("prodeje.txt", mode="w")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Kino:
    def __init__(self, nazev_filmu, kapacita):
        self.nazev_filmu = nazev_filmu
        self.kapacita = kapacita
        self.prodano = 0
        logger.info(f"Bylo vytvoreno kino pro film {self.nazev_filmu} s kapacitou {self.kapacita}")

    def koupit_listky(self, pocet):
        logger.debug(f"Osoba chce koupit {pocet} listku")
        # Kontrola vstupů
        if pocet <= 0:
            logger.warning(f"Pocet listku je mensi nez 1")
            raise ValueError("Musíte koupit alespoň 1 lístek.")
        
        
        # Kontrola kapacity
        if (self.prodano + pocet) > self.kapacita:
            logger.error(f"Nedostatek listku, potreba {pocet}, kapacita {self.kapacita} ")
            raise ValueError("Kino je plné nebo není dostatek míst.")

        # Prodej
        self.prodano += pocet
        zbyva = self.kapacita - self.prodano
        logger.info(f"Prodano {self.prodano}, zbyva{zbyva}")
        return zbyva

    def storno_listku(self, pocet):
        if pocet <= 0:
            raise ValueError("Nelze stornovat 0 nebo méně lístků.")
        
        if (self.prodano - pocet) < 0:
            raise ValueError("Nelze stornovat více lístků, než je prodáno.")

        self.prodano -= pocet
        return self.prodano
    

class TestKina(unittest.TestCase):
    def setUp(self):
        self.kino = Kino("film1", 100)
        
    def test_uspesny_nakup(self):
        self.kino.koupit_listky(10)
        self.assertEqual(self.kino.prodano, 10)
        
    def test_plne_kino(self):
        self.kino.koupit_listky(100)
        with self.assertRaises(ValueError):
            self.kino.koupit_listky(1)
    
    def test_storno(self):
        self.kino.koupit_listky(10)
        self.kino.storno_listku(5)
        self.assertEqual(self.kino.prodano, 5)
        
        
if __name__ == "__main__":
    unittest.main()