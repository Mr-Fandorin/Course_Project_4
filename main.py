from src.api import HH
from src.filter import filter_vacancies
from src.vacancies import Vacancy
from src.utils import JSONFileWorker

def main():
    "Основная функция взаимодействия с пользователем"
    user_input = input("Введите название вакансии: ")
    user_number = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range = int(input("Введите минимальную зарплату в рублях: "))
    hh_api = HH(user_input)
    file_worker = JSONFileWorker()

    raw_vacancies = hh_api.load_vacancies()
    vacancies = []
    for vac in raw_vacancies:
        # Создаём объект Vacancy и добавляем его в список vacancies
        vacancy = Vacancy(
            name=vac['name'],
            salary=vac['salary'],
            url=vac['alternate_url'],
            responsibility=vac["snippet"]['responsibility']
        )
        vacancies.append(vacancy)

    sorted_dict = sorted(vacancies, reverse=True)


    vacancies_dict = []
    for vac in sorted_dict:
        # Переводим объект Vacancy в словарь и добавляем его в список vacancies_dict
        vacancies_dict.append(vac.cast_to_dict())

    file_worker.save_data(vacancies_dict)

    filtered_vacancies = filter_vacancies([{
        'name': vacancy.name,
        'salary': vacancy.salary,
        'url': vacancy.url,
        'responsibility': vacancy.responsibility
    } for vacancy in sorted_dict], salary_range)
    print('Отфильтрованные вакансии: ')
    for vacancy in filtered_vacancies[:user_number]:
        print(f'Название вакансии: {vacancy['name']}, Зарплата: {vacancy['salary']} рублей, URL: {vacancy['url']}, Описание: {vacancy['responsibility']}')



main()