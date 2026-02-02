import pytest

from src.vacancies import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("Тестировщик комфорта квартир", {"from":350000,"to":None,"currency":"RUR","gross":False}, "https://hh.ru/vacancy/93353083",
                   "Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты в спальне.")


@pytest.fixture
def vacancy_2():
    return Vacancy("Удаленный специалист службы поддержки", {"from":100000,"to":None,"currency":"RUR","gross":False}, "https://hh.ru/vacancy/92223870",
                   "Работать с клиентами или партнерами для решения разнообразных ситуаций.")


@pytest.fixture
def vacancy_3():
    return Vacancy("Менеджер по продажам недвижимости", 500000, "https://hh.ru/vacancy/92752367",
                   "Анализ рынка и объектов недвижимости.")


@pytest.fixture
def vacancy_4():
    return Vacancy("Оператор ПК, оператор базы данных", {"from":350000,"to":None,"currency":"RUR","gross":False}, "https://hh.ru/vacancy/93166058",
                   "Расширение клиентской базы. Проведение презентаций и переговоров.")


# @pytest.fixture
# def salary():
#     return Vacancy
# "salary":{"from":350000,"to":450000,"currency":"RUR","gross":false}