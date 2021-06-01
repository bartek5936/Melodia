class Cars:

    def __init__(self, car_brand, car_model, production_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.production_year = production_year
        self.cars_data = {'car_brand': self.car_brand,
                          'car_model': car_model,
                          'production_year': production_year}

    def add_car_to_data(self,  ):

        pass

    def write_cars_to_file(self, file_path):
        # zapisz do pliku wszystkie samochody z cars_data
        pass

    def show_all_cars_in_konsole(self):
        # wyświetl wszystkie samochody ze słownika (wyświetl w tabeli)
        pass

    def download_data_from_file(self):
        # pobierz dane z pliku
        pass