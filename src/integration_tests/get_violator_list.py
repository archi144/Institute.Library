import pytest
import datetime

def get_violators(violators):
    print(violators)

class TestGetViolatorList:
    # Тест проверяет запрос и выдачу списка нарушителей библиотеки
    def test_violator_list(self):
        violators = [{'name': 'Артур', 'surname': 'Мечетин', 'bilet': '521251631'},
                     {'name': 'Марк', 'surname': 'Фолькин', 'bilet': '125126126'},
                     {'name': 'Дастан', 'surname': 'Наубетов', 'bilet': '125126316'},
                     {'name': 'Алексей', 'surname': 'Алексеев', 'bilet': '253251613'}]
        get_violators(violators)
