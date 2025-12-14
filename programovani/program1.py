import logging
import unittest

logger = logging.getLogger("coffee_app")
console_output = logging.StreamHandler()
console_output.setLevel(logging.WARNING)
logger.setLevel(logging.DEBUG)
logger.addHandler(console_output)

file_handler = logging.FileHandler("kavovar_history.log", mode="w")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_format = logging.Formatter('%(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
console_output.setFormatter(console_format)



class Kavovar():
    def __init__(self, max_voda, max_zrna):
        self.voda = 0
        self.zrna = 0
        self.max_voda = max_voda
        self.max_zrna = max_zrna
        logger.info(f"Kavovar byl vytvoren s kapacitou vody {max_voda} a zrna {max_zrna}")
        
    def doplnit_vodu(self, mnozstvi):
        zustatek_kapacity = self.max_voda - self.voda
        
        if mnozstvi <= 0:
            logger.warning(f"Mnozstvi vody je {mnozstvi}, musi byt vetsi nez 0")
            raise ValueError("Objem musi byt vetsi nez 0")
        
        if mnozstvi > zustatek_kapacity:
            logger.error(f"Presahli jste kapacitu nadrze, vejde se max{zustatek_kapacity}")
            raise ValueError("Objem presahuje objem nadrze")
        
        logger.info(f"Bylo pridano {mnozstvi}ml vody")
        self.voda += mnozstvi
        
    def doplnit_zrna(self, mnozstvi):
        zustatek_kapacity = self.max_zrna - self.zrna
                
        if mnozstvi <= 0:
            logger.warning(f"Mnozstvi zrna je {mnozstvi}, musi byt vetsi nez 0")
            raise ValueError("Mnozstvi musi byt vetsi nez 0")
        
        if mnozstvi > zustatek_kapacity:
            logger.error(f"Presahli jste kapacitu nadrze, vejde se max{zustatek_kapacity}")
            raise ValueError("Mnozstvi presahuje kapacitu nadrze")
        
        logger.info(f"Bylo pridano {mnozstvi}g zrna")  
        self.zrna += mnozstvi
        
    def udelat_espresso(self):
        mnozstvi_vody = 30
        mnozstvi_zrna = 7
        logger.debug(f"Priprava espressa")
        
        if self.voda < mnozstvi_vody:
            logger.error(f"Nedostatek vody v nadrzi")
            raise ValueError("Nedostatek vody v nadrzi")
        if self.zrna < mnozstvi_zrna:
            logger.error(f"Nedostatek zrna v nadrzi")
            raise ValueError("Nedostatek zrna v nadrzi")
        
        self.voda -= mnozstvi_vody
        self.zrna -= mnozstvi_zrna
        logger.info("Espreso je hotovo")
        return "Vase kava je hotova"
        
class TestKavovaru(unittest.TestCase):
    
    def setUp(self):
        self.kavovar = Kavovar(1000, 200)
        
    def test_doplneni_vody(self):
        self.kavovar.doplnit_vodu(500)
        self.assertEqual(self.kavovar.voda, 500)
        
    def test_doplneni_zrna(self):
        self.kavovar.doplnit_zrna(100)
        self.assertEqual(self.kavovar.zrna, 100)
        
    def test_preteceni_vody(self):
        self.kavovar.doplnit_vodu(1000)
        with self.assertRaises(ValueError):
            self.kavovar.doplnit_vodu(1)
            
    def test_preteceni_zrna(self):
        self.kavovar.doplnit_zrna(200)
        with self.assertRaises(ValueError):
            self.kavovar.doplnit_zrna(1)
            
    def test_uspesne_espreso(self):
        self.kavovar.doplnit_vodu(400)
        self.kavovar.doplnit_zrna(50)
        self.kavovar.udelat_espresso()
        self.assertEqual(self.kavovar.voda, 370)
        self.assertEqual(self.kavovar.zrna, 43)

    def test_chybi_zrna(self):
        self.kavovar.doplnit_vodu(300)
        with self.assertRaises(ValueError):
            self.kavovar.udelat_espresso()
            
    def test_chybi_voda(self):
        self.kavovar.doplnit_zrna(20)
        with self.assertRaises(ValueError):
            self.kavovar.udelat_espresso()
            
if __name__ == "__main__":
    unittest.main()
    
    