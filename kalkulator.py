import datetime

print("Kalkulator")
b = "1"
while not b == '0':
    aa = input("Podaj co chcesz robic \n 1. Dodawania \n 2. Odejmowanie \n 3. Mnozenie\n 4. Dzielenie\n")
    a = int(input("Podaj liczbe"))
    b = int(input("Podaj liczbe"))
    wynik = 0

    if aa == '1':
        wynik = a + b
        print(wynik)
    if aa == '2':
        wynik = a - b
        print(wynik)
    if aa == '3':
        wynik = a*b
        print(wynik)
    if aa == "4":
        try:
            wynik = a / b
            print(wynik)
        except (ZeroDivisionError):

            print("nie dziel przez zero")

    plik = open("wynikdzi2alania.txt", "w")
    plik.write(str(wynik))
    if b == 0:
        break
print("koniec dzialania")
print("dziekuje")

