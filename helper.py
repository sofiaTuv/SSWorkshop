import string
from faker import Faker

faker = Faker()


class Helper:

    @staticmethod
    def generate_code():
        return faker.random_number(digits=10)

    @staticmethod
    def generate_last_name():
        return faker.last_name()

    @staticmethod
    def generate_name(postcode):
        alphabet = string.ascii_lowercase
        result = ''
        postcode_str = str(postcode)
        # разбиваем на двузначные цифры
        for i in range(0, len(postcode_str), 2):
            digit = int(postcode_str[i:i + 2])
            result += alphabet[digit % 26]
        first_name = result.capitalize()
        return first_name
