"""módulo para comprobar funcionalidad de programa si año es bisiesto o no"""


def find_leap_year(str_leap_year):
    leap_year = int(str_leap_year)
    if (leap_year % 400 == 0 and leap_year % 4 == 0) or (leap_year % 100 != 0 and leap_year % 4 ==0):
        return "El año {} SI es bisiesto.".format(leap_year)
    else:
        return "El año {} NO es bisiesto.".format(leap_year)