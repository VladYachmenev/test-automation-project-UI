from data.data import Person, Person2
from faker import Faker

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
