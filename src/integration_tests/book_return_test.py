import pytest
import datetime

class TestBookReturn:
    # Тест проверяет ситуацию, когда читатель возвращает книгу, а его читательского билета нет в БД
    def test_reader_not_exist(self):
        reader = {'name':'Артур','surname':'Мечетин','bilet':'521251631'}
        bilets = ['12512516','125136754','346373236']
        if reader['bilet'] not in bilets:
            assert True

    def test_reader_exist(self):
        # Тест проверяет ситуацию, когда читатель возвращает книгу и он есть в БД
        reader = {'name': 'Артур', 'surname': 'Мечетин', 'bilet': '521251631'}
        bilets = ['521251631', '125136754', '346373236']
        if reader['bilet'] in bilets:
            assert True

    def test_return_intime_book(self):
        # Тест проверяет возврат книги после успешной идентификации пользовател

        reader = {'name': 'Артур', 'surname': 'Мечетин', 'bilet': '521251631',
                  'books':[{'author':'Glitch','title':'Glitch Adventures','type':'PAPER','return_date':(2020,1,12)},
                           {'author':'Garry','title':'Garry Adventures','type':'ELECTRONIC','url':'https://someurl','return_date':(2020,1,12)}]
                  }
        shouldReturnBooks = [{'author':'Glitch','title':'Glitch Adventures','type':'PAPER','return_date':(2020,1,7)},
                           {'author':'Garry','title':'Garry Adventures','type':'ELECTRONIC','url':'https://someurl','return_date':(2020,1,14)},
                             {'author':'James','title':'James Adventures','type':'PAPER','return_date':(2020,1,17)}]
        indexes = list()
        for index,i in enumerate(shouldReturnBooks,0):
            for value in reader['books']:
                if i['title'] in value['title']:
                    indexes.append(index)
                    if i['return_date'] < value['return_date']:
                        print("Возврат книги {} просрочен, пользователь {} объявлен нарушителем".format(i['title'],
                                                                                                        reader[
                                                                                                            'name'] + " " +
                                                                                                        reader[
                                                                                                            'surname']))

        for i in indexes:
            del shouldReturnBooks[i]
        assert len(shouldReturnBooks) == 1
