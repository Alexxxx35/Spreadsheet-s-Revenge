from faker import Faker
import random
import json
import time
import requests
import pandas as pd
import os


class data:
    def __init__(self, number_of_row) -> None:
        self.number_of_row = number_of_row
        self.timer = 1

    def fake_data(self) -> list:
        i = 0
        car_api_url = 'https://parseapi.back4app.com/classes/Car_Model_List'
        headers = {
            # This is the fake app's application id
            'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z',
            # This is the fake app's readonly master key
            'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW'
        }
        car_data = json.loads(requests.get(car_api_url, headers=headers).content.decode(
            'utf-8'))
        self.data = []
        faker = Faker()
        phone = "0"+str(random.randint(6, 7))
        while i < self.number_of_row:
            self.profile = faker.simple_profile()
            self.profile["birthdate"] = str(self.profile["birthdate"])
            for index, element in enumerate(range(8)):
                element = random.randint(1, 9)
                if index % 2 == 0:
                    phone += " "
                phone += str(element)
            self.profile["phone_number"] = phone
            self.profile["job"] = faker.job()
            self.profile["credit_card_povider"] = faker.credit_card_provider()
            self.profile["IBAN"] = faker.iban()
            self.profile["credit_card_number"] = faker.credit_card_number()
            self.profile["security code"] = faker.credit_card_security_code()
            self.profile["expires"] = faker.credit_card_expire()
            self.profile["balance"] = random.uniform(1.0, 100000.0)
            self.profile["currency_balance"] = faker.currency_name()
            self.profile["currency_balance_code"] = faker.currency_code()
            random_car = random.choice(car_data["results"])
            self.profile["car_model"] = random_car["Model"]
            self.profile["car_maker"] = random_car["Make"]
            self.profile["car_year_making"] = random_car["Year"]
            self.profile["car_color"] = faker.hex_color()
            self.profile["car_licence"] = faker.license_plate()
            self.profile["car_product_ean"] = faker.ean(length=13)
            self.profile["compagny_name"] = faker.company().replace(",", "") + \
                faker.company_suffix()
            self.profile["compagny_purpose"] = faker.bs()
            self.profile["compagny_address"] = faker.address()
            data.append(self.profile)
            i += 1
            print(json.dumps(data))
            time.sleep(self.timer)
        return json.dumps(data)

    def csv_builder(self, data: str, csv_path: str, append: bool):
        if append:
            mode = 'a'
            header = False
        else:
            mode = 'w'
            header = True
        df = pd.DataFrame(json.loads(data))
        df.to_csv(csv_path, index=False, sep=",", mode=mode, header=header)
        print(df)


d = data()
d.csv_builder(d.fake_data(10), os.path.join("csv", "data.csv"), True)
