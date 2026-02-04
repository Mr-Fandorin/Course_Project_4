from src.filter import filter_vacancies


def test_filter_vacancies_min_salary(sample_vacancies):
    result = filter_vacancies(sample_vacancies, min_salary=60000)
    assert len(result) == 2
