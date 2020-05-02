"""test pruebas para main.py de comprobar si año bisiesto"""

import unittest#importar para test de pruebas
import leap_year_module#importar para comprobar funcionalidad del programa

class Leap_year_test(unittest.TestCase):

    def test_leap_year(self):
        self.assertEqual(leap_year_module.find_leap_year(2004), "El año 2004 SI es bisiesto.")
        self.assertEqual(leap_year_module.find_leap_year(1972), "El año 1972 SI es bisiesto.")
        self.assertEqual(leap_year_module.find_leap_year(1984), "El año 1984 SI es bisiesto.")
        self.assertEqual(leap_year_module.find_leap_year(1996), "El año 1996 SI es bisiesto.")
        self.assertEqual(leap_year_module.find_leap_year(2008), "El año 2008 SI es bisiesto.")
        self.assertEqual(leap_year_module.find_leap_year(2012), "El año 2012 SI es bisiesto.")
        self.assertEqual(leap_year_module.find_leap_year(2100), "El año 2100 NO es bisiesto.")
        self.assertEqual(leap_year_module.find_leap_year(2200), "El año 2200 NO es bisiesto.")
        self.assertEqual(leap_year_module.find_leap_year(2300), "El año 2300 NO es bisiesto.")

if __name__ == "__main__":
    unittest.main()