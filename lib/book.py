#!/usr/bin/env python3

class Book:
    def __init__(self, title="And Then There Were None", page_count=272):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError("Title must be a string.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

my_book = Book("And Then There Were None", 272)
print(my_book.title)
print(my_book.page_count)