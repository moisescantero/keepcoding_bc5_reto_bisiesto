"""test pruebas para main.py de comprobar si año bisiesto"""

import unittest#importar para test de pruebas
import leap_year_module#importar para comprobar funcionalidad del programa

class Leap_year_test(unittest.TestCase):

    def test_leap_year(self):
        self.assertEqual(leap_year_module.find_leap_year(2004), 'hola')
        self.assertEqual(leap_year_module.find_leap_year(1972), True)
        self.assertEqual(leap_year_module.find_leap_year(1984), True)
        self.assertEqual(leap_year_module.find_leap_year(1996), True)
        self.assertEqual(leap_year_module.find_leap_year(2008), True)
        self.assertEqual(leap_year_module.find_leap_year(2012), True)
        self.assertEqual(leap_year_module.find_leap_year(2100), False)
        self.assertEqual(leap_year_module.find_leap_year(2200), False)
        self.assertEqual(leap_year_module.find_leap_year(2300), False)
        self.assertEqual(leap_year_module.find_leap_year(1600), True)
        self.assertEqual(leap_year_module.find_leap_year(2000), True)
        self.assertEqual(leap_year_module.find_leap_year(2400), True)

