from faker import Faker
import random
import json
import time
import requests
import pandas as pd
import os


def fake_data(number_of_row: int, timer: int) -> list:
    i = 0
    car_api_url = 'https://parseapi.back4app.com/classes/Car_Model_List'
    headers = {
        # This is the fake app's application id
        'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z',
        # This is the fake app's readonly master key
        'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW'
    }
    car_data = json.loads(requests.get(car_api_url, headers=headers).content.decode(
        'utf-8'))  # Here you have the data that you needs
    data = []
    faker = Faker()
    phone = "0"+str(random.randint(6, 7))
    while i < number_of_row:
        profile = faker.simple_profile()
        profile["birthdate"] = str(profile["birthdate"])
        for index, element in enumerate(range(8)):
            element = random.randint(1, 9)
            if index % 2 == 0:
                phone += " "
            phone += str(element)
        profile["phone_number"] = phone
        profile["job"] = faker.job()
        profile["credit_card_povider"] = faker.credit_card_provider()
        profile["IBAN"] = faker.iban()
        profile["credit_card_number"] = faker.credit_card_number()
        profile["security code"] = faker.credit_card_security_code()
        profile["expires"] = faker.credit_card_expire()
        profile["balance"] = random.uniform(1.0, 100000.0)
        profile["currency_balance"] = faker.currency_name()
        profile["currency_balance_code"] = faker.currency_code()
        random_car = random.choice(car_data["results"])
        profile["car_model"] = random_car["Model"]
        profile["car_maker"] = random_car["Make"]
        profile["car_year_making"] = random_car["Year"]
        profile["car_color"] = faker.hex_color()
        profile["car_licence"] = faker.license_plate()
        profile["car_product_ean"] = faker.ean(length=13)
        profile["compagny_name"] = faker.company().replace(",", "") + \
            faker.company_suffix()
        profile["compagny_purpose"] = faker.bs()
        profile["compagny_address"] = faker.address()
        data.append(profile)
        i += 1
        print(json.dumps(data))
        time.sleep(timer)
    return json.dumps(data)


def csv_builder(data, csv_path: str, append: bool):
    if append:
        mode = 'a'
        header = False
    else:
        mode = 'w'
        header = True
    df = pd.DataFrame(json.loads(data))
    df.to_csv(csv_path, index=False, sep=",", mode=mode, header=header)
    print(df)


csv_builder(fake_data(1, 1), os.path.join("csv", "data.csv"), True)
