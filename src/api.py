from abc import ABC, abstractmethod

import requests


class API(ABC):

    @abstractmethod
    def _api_connect(self, keyword):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass


class HH(API):
    def __init__(self, keyword):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'text': keyword, 'page': 0, 'per_page': 100, 'only_with_salary': True, 'currency': 'RUR'}
        self.__vacancies = []


    def _api_connect(self, keyword):
        self.__params['text'] = keyword
        response = requests.get(self.__url, params=self.__params)
        if response.status_code != 200:
            raise ValueError("Failed to get info")
        return response

    def load_vacancies(self):
        while self.__params.get('page') != 20:
            vacancies = self._api_connect(self.__params['text']).json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
        return self.__vacancies



if __name__ == "__main__":
    a = HH('python')
    print(a.load_vacancies())

