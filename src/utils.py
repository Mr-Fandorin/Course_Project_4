import json
from abc import ABC, abstractmethod


class FileWorker(ABC):
    "Абстрактный класс для работы с файлом"

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def save_data(self, new_data):
        pass

    @abstractmethod
    def file_delete(self):
        pass


class JSONFileWorker(FileWorker):
    "Класс для работы с файлом JSON"

    def __init__(self, filename: str = "vacancies.json"):
        self.filename = filename

    def get_data(self):
        "Получение данных из файла"
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self, new_data: list[dict[str, (int | str)]]):
        "Добавление данных в файл"
        # Получаем данные из файла (старые вакансии)
        old_data = self.get_data()
        # Проходим по каждой новой вакансии
        for vacancy in new_data:
            # Флаг для проверки на дубликаты
            is_duplicate = False
            # Проходим по каждой старой вакансии
            for old_vacancy in old_data:
                # Сравниваем URL
                if vacancy["url"] == old_vacancy["url"]:
                    # Если URL совпадает, то это дубликат
                    is_duplicate = True
                    # Если дубликат, то выходим из внутреннего цикла
                    break
            # Если это не дубликат, то добавляем вакансию в список старых
            if not is_duplicate:
                old_data.append(vacancy)

        # Сохраняем данные в файл
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(old_data, f, ensure_ascii=False, indent=2)

    def file_delete(self):
        "Удаление данных из файла"
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
