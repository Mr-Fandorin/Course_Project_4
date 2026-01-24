from src.api import HH


class Vacancies:


    __slots__ = ('name', '_salary', 'url', 'responsibility')

    def __init__(self, name, salary, url, responsibility):
        self.name = name
        self._salary = salary
        self.url = url
        self.responsibility = responsibility

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if type(value['from']) is int:
            if type(value['to']) is int:
                self._salary = (value['to'] + value['from']) / 2

            else:
                self._salary = value['from']

        elif type(value['to']) is int:
            self._salary = value['to']

        else:
            self._salary = 0


    def __gt__(self, other):
        return self.salary > other
    def __lt__(self, other):
        return self.salary < other
    def __ge__(self, other):
        return self.salary >= other
    def __le__(self, other):
        return self.salary <= other

    def cast_to_dict(self):
        return {'name': self.name, 'salary': self.salary, 'url': self.url, 'responsibility': self.responsibility}



raw_vacancies = HH.load_vacancies()
vacancy_objects = []
for vac in raw_vacancies:
    v = Vacancies(name=vac['name'], salary=vac['salary'], url=vac['alternate_url'], responsibility=vac['responsibility'])
    vacancy_objects.append(v)

