"""main comprobar si año es bisiesto o no:
Un año es bisiesto si es múltipo de cuatro (1982) a no ser que acabe en 00 (múltiplo de 100). En ese caso (tb es múltiplo de 4) puede ser
bisiesto o no. Sólo son bisiesto los acabados en 00 y múltiplos de 400 (el 2000 es bisiesto) pero no son bisiestos los acabados en 00 y
NO multiplos de 400, por ejemplo 1900 no es bisiesto, igual que 1800 o 1700 tampoco son bisiestos, pero 1600 si lo es porque es múltipo 
de 400.
Test de pruebas: SI 2004 2008 2012
                NO 2100 2200 2300
                SI 1600 2000 2400"""


import leap_year_module

result_leap_year = leap_year_module.find_leap_year(input("Introduzca año: "))
print(result_leap_year)











