import json
from abc import ABC, abstractmethod


class FileWorker(ABC):


    @abstractmethod
    def file_get(self):
        pass

    @abstractmethod
    def file_save(self, filename):
        pass

    @abstractmethod
    def file_delete(self):
        pass

class JSONFileWorker(FileWorker):

    def __init__(self, filename: str = "vacancies.json"):
        self.vacancy = []
        self.filename = filename

    def file_get(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def file_save(self, newdate):
       vacancies_data = self.file_get()

        # if isinstance(vacancies_data, dict):
        #     vacancies_data = []

        filtered_date = []
        for item in newdate:
            for vac in vacancies_data:
                if item["url"] == vac["url"]:
                    filtered_date.append(item)

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(filtered_date, f, ensure_ascii=False, indent=4)


    def file_delete(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)



