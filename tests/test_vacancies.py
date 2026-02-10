def test_salary_setter(vacancy):
    salary_dict = {"from": 0, "to": 350000, "currency": "RUR", "gross": "false"}
    vacancy.salary = salary_dict
    assert vacancy.salary == 175000


def test_vacancies_eq(vacancy, vacancy_4):
    assert vacancy == vacancy_4


def test_vacancies_gt(vacancy, vacancy_2):
    assert vacancy > vacancy_2


def test_vacancies_lt(vacancy_2, vacancy):
    assert vacancy_2 < vacancy


def test_cast_to_dict(vacancy):
    result = vacancy.cast_to_dict()
    assert result == {
        "name": "Тестировщик комфорта квартир",
        "salary": 350000,
        "url": "https://hh.ru/vacancy/93353083",
        "responsibility": "Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты в спальне.",
    }
