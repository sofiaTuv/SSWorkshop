import string
from faker import Faker

faker = Faker()


def generate_code():
    return faker.random_number(digits=10)


def generate_last_name():
    return faker.last_name()


def generate_name(postcode):
    alphabet = string.ascii_lowercase
    result = ''
    postcode_str = str(postcode)
    # разбиваем на двузначные цифры
    for i in range(0, len(str(postcode_str)), 2):
        code = postcode_str[i:i + 2]
        # проверяем, является ли символ числом
        if code.isdigit():
            index = int(i) % 26
            result += alphabet[index]
    return result
