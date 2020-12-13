from lab_3_zad_1.Menu import Menu

"""Proszę zbudować program który
1. Bedzie obliczał pola figur:
    Kwadrat
    Prostokąt
    Koło
    Trójkąt
    Trapez
2. Użytkownik będzie dokonywał wyboru która figura ma być obliczona
3. Program ma trzymać log operacji w postaci listy (wybór operacji, data igodzina działąnia)"""

menu = Menu()
menu.show()

while (True):
    menu.get_select()
