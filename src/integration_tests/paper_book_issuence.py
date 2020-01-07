import pytest
import datetime

class TestBookReturn:

    def test_paper_book_not_exist(self):
        # Тест проверяет ситуацию, когда запрашиваемая электронная версия книги отсутствует в БД
        books_what_reader_needs = [{'author':'John','title':'John Adventures','type':'PAPER'}]
        exists_books = [{'author':'Garry','title':'Garry Adventures','type':'PAPER','count': 5},
                        {'author':'Jack','title':'Jack Adventures','type':'PAPER','count': 2},
                        {'author':'Willy','title':'Willy Adventures','type':'ELECTRONIC','url':'https://willyurl'}]

        for book_need in books_what_reader_needs:
            bookExist = False
            for book_exist in exists_books:
                value = list(book_need.values())
                values = list(book_exist.values())[:-1]
                if  value == values and book_exist['count'] > 0:
                    bookExist = True
                    break
            if bookExist:
                print(f"Книга {book_need['title']} есть в бумажном варианте")
                assert False
            else:
                print(f"Книги {book_need['title']} в бумажном варианте нет")
                assert True
    def test_paper_book_exist_but_not_count(self):
        # Тест проверяет ситуацию, когда запрашиваемая электронная версия книги есть в БД, но отсутствует в библотеке
        books_what_reader_needs = [{'author':'John','title':'John Adventures','type':'PAPER'}]
        exists_books = [{'author':'John','title':'John Adventures','type':'PAPER','count': 0},
                        {'author':'Jack','title':'Jack Adventures','type':'PAPER','count': 2},
                        {'author':'Willy','title':'Willy Adventures','type':'ELECTRONIC','url':'https://willyurl'}]

        for book_need in books_what_reader_needs:
            bookExist = False
            for book_exist in exists_books:
                value = list(book_need.values())
                values = list(book_exist.values())[:-1]
                if  value == values and book_exist['count'] > 0:
                    bookExist = True
                    break
            if bookExist:
                print(f"Книга {book_need['title']} есть в бумажном варианте")
                assert False
            else:
                print(f"Книги {book_need['title']} в бумажном варианте нет")
                assert True

    def test_paper_book_exist(self):
        # Тест проверяет ситуацию, когда запрашиваемая бумажная версия книги есть в БД
        books_what_reader_needs = [{'author': 'John', 'title': 'John Adventures', 'type': 'PAPER'}]
        exists_books = [{'author': 'John', 'title': 'John Adventures', 'type': 'PAPER', 'count': 5},
                        {'author': 'Jack', 'title': 'Jack Adventures', 'type': 'PAPER', 'count': 2},
                        {'author': 'Willy', 'title': 'Willy Adventures', 'type': 'ELECTRONIC',
                         'url': 'https://willyurl'}]

        for book_need in books_what_reader_needs:
            bookExist = False
            for book_exist in exists_books:
                value = list(book_need.values())
                values = list(book_exist.values())[:-1]
                if value == values and book_exist['count'] > 0:
                    bookExist = True
                    break
            if bookExist:
                print(f"Книга {book_need['title']} есть в бумажном варианте")
                assert True
            else:
                print(f"Книги {book_need['title']} в бумажном варианте нет")
                assert False


    def test_paper_booksuance(self):
        # Тест проверяет выдачу печатной книги пользователю
        books_what_reader_needs = [{'author':'Garry','title':'Garry Adventures','type':'PAPER'},
                                   {'author': 'Willy', 'title': 'Willy Adventures', 'type': 'PAPER'}]
        reader = {'name':'Артур','surname':'Мечетин','bilet':'521251631', 'books': None}
        exists_books = [{'author': 'Garry', 'title': 'Garry Adventures', 'type': 'PAPER', 'count': 2 },
                        {'author': 'Jack', 'title': 'Jack Adventures', 'type': 'ELECTRONIC', 'url': 'https://jackyurl'},
                        {'author': 'Willy', 'title': 'Willy Adventures', 'type': 'PAPER','count': 3 }]
        array_of_books = list()
        for book_need in books_what_reader_needs:
            for book_exist in exists_books:
                value = list(book_need.values())
                values = list(book_exist.values())[:-1]
                if value == values and book_exist['count'] > 0:
                    print(f"Книга {book_need['title']} есть в бумажном варианте")
                    print("Выдаем книгу на условленный срок...")
                    getting_book = book_exist
                    link_life = datetime.date.today() + datetime.timedelta(days=14)
                    getting_book.update({'link_life':link_life})
                    array_of_books.append(getting_book)
                    print(reader)
                    break
                else:
                    pass
        reader.update({'books': array_of_books})
        if len(reader['books']) == 2:
            assert True
        else:
            assert False