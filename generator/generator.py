from data.data import Person, Person2,NewPerson
from faker import Faker
import random
faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.language_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def generated_person2():
    yield Person2(
        full_name=faker_ru.first_name(),
        email=faker_ru.first_name(),
        current_address=faker_ru.first_name(),
        permanent_address=faker_ru.first_name(),

    )


def generated_new_person():
    yield NewPerson(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(10,90),
        salary=random.randint(1000,90000),
        department=faker_ru.city(),
        invalid_email=faker_ru.url()
    )
