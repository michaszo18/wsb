from unittest import TestCase

from classes.GuestBook import GuestBook


class TestGuestBook(TestCase):

    def setUp(self):
        self.cut = GuestBook("Mike")


