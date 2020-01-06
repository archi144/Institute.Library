import pytest
import datetime

class TestBookReturn:
    # Тест проверяет ситуацию, когда  при обращении читателя к библиотеке у читательского билета истек срок годности
    def test_bilet_expired(self):
        reader = {'name':'Артур','surname':'Мечетин','bilet':'521251631'}
        bilets = [{'id':'521251631','date':(2020,5,21)},{'id':'12512615','date':(2020,6,21)},{'id':'1231523512','date':(2020,4,21)}]
        current_date = (2020,8,29)
        for i in bilets:
            if i.get('id') == reader['bilet']:
                if i.get('date') < current_date:
                    print(f"Срок действия билета с номером {i.get('id')} истек")
                    assert True

    def test_bilet_not_expired(self):
        # Тест проверяет ситуацию, когда  при обращении читателя к библиотеке у читательского билета не истек срок годности
        reader = {'name': 'Артур', 'surname': 'Мечетин', 'bilet': '521251631'}
        bilets = [{'id': '521251631', 'date': (2020, 5, 21)}, {'id': '12512615', 'date': (2020, 6, 21)},
                  {'id': '1231523512', 'date': (2020, 4, 21)}]
        current_date = (2020, 8, 29)
        for i in bilets:
            if i.get('id') == reader['bilet']:
                if i.get('date') > current_date:
                    assert True

    def test_electronic_book_not_exist(self):
        # Тест проверяет ситуацию, когда запрашиваемая электронная версия книги отсутствует в ЬД
        books_what_reader_needs = [{'author':'Garry','title':'Garry Adventures','type':'ELECTRONIC'}]
        exists_books = [{'author':'Garry','title':'Garry Adventures','type':'PAPER','count':'5'},
                        {'author':'Jack','title':'Jack Adventures','type':'PAPER','count':'2'},
                        {'author':'Willy','title':'Willy Adventures','type':'ELECTRONIC','url':'https://willyurl'}]

        for book_need in books_what_reader_needs:
            bookExist = False
            for book_exist in exists_books:
                value = list(book_need.values())
                values = list(book_exist.values())[:-1]
                if  value == values:
                    bookExist = True
                    break
            if bookExist:
                print(f"Книга {book_need['title']} есть в электронном варианте")
                assert False
            else:
                print(f"Книги {book_need['title']} в электронном варианте нет")
                assert True

    def test_electronic_book_exist(self):
        # Тест проверяет ситуацию, когда запрашиваемая электронная версия книги есть в ЬД
        books_what_reader_needs = [{'author':'Garry','title':'Garry Adventures','type':'ELECTRONIC'}]
        exists_books = [{'author':'Garry','title':'Garry Adventures','type':'ELECTRONIC','count':'5'},
                        {'author':'Jack','title':'Jack Adventures','type':'PAPER','count':'2'},
                        {'author':'Willy','title':'Willy Adventures','type':'ELECTRONIC','url':'https://willyurl'}]

        for book_need in books_what_reader_needs:
            bookExist = False
            for book_exist in exists_books:
                value = list(book_need.values())
                values = list(book_exist.values())[:-1]
                if  value == values:
                    bookExist = True
                    break
            if bookExist:
                print(f"Книга {book_need['title']} есть в электронном варианте")
                assert True
            else:
                print(f"Книги {book_need['title']} в электронном варианте нет")
                assert False


    def test_electronic_booksuance(self):
        # Тест проверяет выдачу электронной книги пользователю
        books_what_reader_needs = [{'author':'Garry','title':'Garry Adventures','type':'ELECTRONIC'},
                                   {'author': 'Willy', 'title': 'Willy Adventures', 'type': 'ELECTRONIC'}]
        reader = {'name':'Артур','surname':'Мечетин','bilet':'521251631', 'books': None}
        exists_books = [{'author': 'Garry', 'title': 'Garry Adventures', 'type': 'ELECTRONIC', 'url': 'https://garryurl'},
                        {'author': 'Jack', 'title': 'Jack Adventures', 'type': 'PAPER', 'count': '2'},
                        {'author': 'Willy', 'title': 'Willy Adventures', 'type': 'ELECTRONIC','url': 'https://willyurl'}]

        for book_need in books_what_reader_needs:
            for book_exist in exists_books:
                value = list(book_need.values())
                values = list(book_exist.values())[:-1]
                if value == values:
                    print(f"Книга {book_need['title']} есть в электронном варианте")
                    print("Выдаем книгу на условленный срок...")
                    getting_book = book_exist
                    link_life = datetime.date.today() + datetime.timedelta(days=14)
                    getting_book.update({'link_life':link_life})
                    reader.update({'books': getting_book})
                    print(reader)
                    break
                else:
                    pass
        if reader['books'] != None:
            assert True
        else:
            assert False