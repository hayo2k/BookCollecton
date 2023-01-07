from abc import ABC, abstractmethod
from library import *

class Books(ABC, Library):
    def __init__(self):
        self.books_dict = dict()
        super().__init__()




    @abstractmethod
    def type_book(self):
        pass

    def add_book(self):
        new_book = input('Введите название книги: ').strip().title()
        book_amount = input('Сколько копий? \n').strip()
        self.book += int(book_amount)

        assert  book_amount.isdigit(), 'Нужно ввести число'

        book_amount = int(book_amount)

        if new_book not in self.books_dict:
            self.books_dict[new_book] = book_amount

        else:
            self.books_dict[new_book] += book_amount

    def get_book(self):
        search_book = input('Введите название книги которую хотите найти: ').strip().title()

        if self.books_dict.setdefault(search_book, None):
            print(f'Количество достуных книг по данному запросу {self.books_dict.get(search_book)} шт')






class Fantasy(Books):
    def type_book(self):
        return 'Фэнтези'

class Detective(Books):
    def type_book(self):
        return 'Детектив'

class Roman(Books):
    def type_book(self):
        return 'Роман'

fantasy = Fantasy()
detect = Detective()
roman = Roman()
fantasy.add_book()
roman.add_book()


print(fantasy.get_book())
print(fantasy.book)
