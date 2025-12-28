import logging
import unittest


# --- 1. ČÁST: ZDE DOPLŇ NASTAVENÍ LOGOVÁNÍ ---
# Potřebujeme:
# - logger jménem "sklad_logger"
# - FileHandler (sklad.log, level DEBUG)
# - StreamHandler (konzole, level INFO)
# - Formatter (např: '%(asctime)s - %(levelname)s - %(message)s')
# - Přiřadit handlery k loggeru

# ... tvůj kód pro logování ...
# (Zatím si vytvoř jen proměnnou 'logger', abychom ji mohli používat dole)
logger = logging.getLogger("sklad_logger") 
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("sklad.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)

console_output = logging.StreamHandler()
console_output.setLevel(logging.INFO)
console_output.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_output)



# --- 2. ČÁST: TŘÍDA SKLAD ---
class Sklad:
    def __init__(self):
        self.zasoby = {}
        logger.info("Vytvořen nový sklad.")

    def naskladnit(self, nazev, pocet):
        if pocet <= 0:
            logger.warning(f"Pokus naskladnit neplatný počet: {pocet}")
            return # Nic neděláme

        logger.debug(f"Naskladňuji {pocet} ks zboží '{nazev}'")
        
        # Zde je logika pro přidání do slovníku
        if nazev in self.zasoby:
            self.zasoby[nazev] += pocet
        else:
            self.zasoby[nazev] = pocet
            
        logger.info(f"Naskladněno: {nazev}, nový stav: {self.zasoby[nazev]}")

    def vyskladnit(self, nazev, pocet):
        logger.debug(f"Požadavek na vyskladnění: {nazev}, kusů: {pocet}")
        if nazev not in self.zasoby:
            logger.error(f"polozka '{nazev}' neni v zasobe")
            raise ValueError("zbozi neni skladem")
        elif self.zasoby[nazev]<pocet:
            aktualni_stav = self.zasoby[nazev]
            logger.warning(f"neni dostatek zbozi {nazev}, na sklade{aktualni_stav}, chcete{pocet}")
            raise ValueError("nedostatek zbozi")
        else:
            
        
        # LOGICKÁ CHYBA + CHYBĚJÍCÍ OŠETŘENÍ
        # Tady chybí kontrola, jestli zboží vůbec existuje!
        # Tady chybí kontrola, jestli nejdu do mínusu!
        
            self.zasoby[nazev] -= pocet # Tohle spadne, pokud nazev neexistuje, nebo půjde do mínusu
            
            logger.info(f"Vyskladněno {pocet} ks '{nazev}'.")


# --- 3. ČÁST: TESTY ---
class TestSkladu(unittest.TestCase):
    def setUp(self):
        # Tato metoda se spustí před každým testem
        self.sklad = Sklad()

    def test_naskladneni(self):
        self.sklad.naskladnit("Rohlík", 10)
        self.assertEqual(self.sklad.zasoby["Rohlík"], 10)

    def test_vyskladneni_ok(self):
        self.sklad.naskladnit("Chleba", 5)
        self.sklad.vyskladnit("Chleba", 2)
        self.assertEqual(self.sklad.zasoby["Chleba"], 3)

    # TENTO TEST ZATÍM SELŽE (protože metoda vyskladnit nemá ošetřenou chybu)
    def test_vyskladneni_chyba(self):
        self.sklad.naskladnit("Máslo", 1)
        with self.assertRaises(ValueError):
            self.sklad.vyskladnit("Máslo", 5) # Chceme vybrat víc, než máme

if __name__ == '__main__':
    # Spustí testy
    unittest.main()