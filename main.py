import os


banner = """

╔═╦═╦══╦══╦═╦╗╔══╦═╦═╦╗
║╔╣╬║╔╗╠══╠╗║║╚╗╔╣║║║║║
║╚╣╗╣╠╣║══╬╩╗║ ║║║║║║║╚╗
╚═╩╩╩╝╚╩══╩══╝ ╚╝╚═╩═╩═╝

┌───────────────────────────────────────────┐
│Разработчик: @Fr31zep ТГК: @crazytoolsoft  │
└───────────────────────────────────────────┘
┌────────────────────────────────────┌─────┐┐
│[1] Поиса по номеру                 │ v.2 ││
│[2] Поиск по IP                     └─────┘│
│[3] DDOS                                   │
│[4] Мануал по доксу                        │
│[5] Мануал по свату                        │
│[6] Мануал по сносу ТГ                     │
│[7] Генератор личности                     │
│[8] Генератор карты                        │
│[9] Поиск по базе данных                   │
│[10] Св@t б@нв0рD                          │
│[11] Информация                            │
│[12] Выход                                 │
└───────────────────────────────────────────┘

"""

print(banner)

choice = input("Введите номер желаемой функции -> ")
if choice == "1":
    os.system("clear")
    from phone import phone

if choice == "2":
    os.system("clear")
    from ip import ip

if choice == "3":
    os.system("clear")
    from ddos import ddos

if choice == "4":
    os.system("clear")
    from doks import doks

if choice == "5":
    os.system("clear")
    from swat import swat

if choice == "6":
    os.system("clear")
    from snos import snos
if choice == "7":
    os.system("clear")
    from generate import generate

if choice == "8":
    os.system("clear")
    from card import card

if choice == "9":
    os.system("clear")
    from searchb import searchb

if choice == "10":
    os.system("clear")
    from antispam import antispam

if choice == "11":
    os.system("clear")
    from info import info

if choice == "12":
    os.system("clear")
    from quit import quit
