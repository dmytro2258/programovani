import logging
import unittest

logger = logging.getLogger("nasa_test")
logger.setLevel(logging.DEBUG)

console_output = logging.StreamHandler()
console_output.setLevel(logging.INFO)
logger.addHandler(console_output)

file_handler = logging.FileHandler("mission_log.txt", mode="w")

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
console_formatter = logging.Formatter('%(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
console_output.setFormatter(console_formatter)

class Raketa():
    def __init__(self, nazev, kapacita_nadrze):
        self.palivo = 0
        self.stav = "V hangaru"
        self.nazev = nazev
        self.kapacita_nadrze = kapacita_nadrze
        logger.info("Raketa byla vytvorena")

    def natankovat(self, mnozstvi):
        dostupno = self.kapacita_nadrze - self.palivo
        if mnozstvi <= 0:
            logger.warning(f"Hodnota paliva musi byt vetsi nez 0, chcete natankovat{mnozstvi}")
            raise ValueError("Mnozstvi musi byt vetsi nez 0")
        if mnozstvi + self.palivo > self.kapacita_nadrze:
            logger.error(f"Preliti, chcete doplnit {mnozstvi}, volne misto {dostupno}")
            raise ValueError("Nelze naplnit vic nez kapacita nadrze")
        logger.info(f"Natankovano {mnozstvi} litru paliva")
        self.palivo += mnozstvi
        self.stav = "Tankovani"

    def pripravit_ke_startu(self):
        if self.palivo != self.kapacita_nadrze:
            logger.error("Malo paliva pro start")
            raise ValueError("Nedostatek paliva")
        else:
            logger.info("Vsechny systemy OK, pripraveno k startu")
            self.stav = "Pripraveno"
    
    def odstartovat(self):
        if self.stav != "Pripraveno":
            logger.critical("Pokus o start bez pripravy")
            raise ValueError("Raketa neni pripravena")
        if self.stav == "Pripraveno":
            logger.info("Uspesny start")
            self.stav = "Ve vesmiru"
            self.palivo = 0
        return "Start OK"
    

class TestRakety(unittest.TestCase):

    def setUp(self):
        self.raketa = Raketa("Apolo", 1000)
    
    def test_spravne_tankovani(self):
        self.raketa.natankovat(500)
        self.assertEqual(self.raketa.palivo, 500)
    
    def test_preplneni(self):
        self.raketa.natankovat(1000)
        with self.assertRaises(ValueError):
            self.raketa.natankovat(1)
        
    def test_start_bez_paliva(self):
        self.raketa.natankovat(5)
        with self.assertRaises(ValueError):
            self.raketa.pripravit_ke_startu()
    
    def test_kompletni_mise(self):
        self.raketa.natankovat(1000)
        self.raketa.pripravit_ke_startu()
        self.raketa.odstartovat()
        self.assertEqual(self.raketa.stav, "Ve vesmiru")
        self.assertEqual(self.raketa.palivo, 0)

if __name__ == "__main__":
    unittest.main()