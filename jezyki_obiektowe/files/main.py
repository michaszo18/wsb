from classes.GuestBook import GuestBook

FILE_NAME = "guests_book.txt"

name = input("What's your name: ")

guest_book = GuestBook(name).save_name()


