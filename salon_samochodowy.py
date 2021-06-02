class Cars:

    def __init__(self, car_brand, car_model, production_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.production_year = production_year
        self.cars_data = {'car_brand': self.car_brand,
                          'car_model': self.car_model,
                          'production_year': self.production_year}

    def add_car_to_data(self):

        pass
    def write_cars_to_file(self, file_path):
        plik = open("samochody.txt", "a")
        return plik.write(file_path + "\n")
        pass

    def show_all_cars_in_konsole(self, samochody):
        return print(samochody)
        pass

    def download_data_from_file(self, plik):
        plik = open("samochody.txt", "r")
        print(plik.read())


        pass
i = input('Podaj liczbe samochodow')
for k in range(int(i)):
    obietk = []
    obiekt = Cars(input(str("Podaj Marke ")), input(str("Podaj model ")), input(str("Podaj date produkcji ")))
    print(obiekt)
    obiekt.write_cars_to_file(str(obiekt))
    obiekt.show_all_cars_in_konsole(str(obiekt))
    obiekt.download_data_from_file(str(obiekt))
    pass
