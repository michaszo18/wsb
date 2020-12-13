from datetime import datetime

from classes.FileManipulation import FileManipulation


class GuestBook:

    def __init__(self, name) -> None:
        self.__fileManipulation = FileManipulation('guest_book.txt')
        self.__name = name

    def save_name(self):
        date_now = datetime.now()
        message = f"{date_now} - Hello {self.__name}\n"
        self.__fileManipulation.add_line(message)
