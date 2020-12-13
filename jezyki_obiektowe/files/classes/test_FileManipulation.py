from unittest import TestCase

from classes.FileManipulation import FileManipulation


class TestFileManipulation(TestCase):

    def setUp(self):
        self.cut = FileManipulation('C:/Users/Mike/PycharmProjects/files/guest_book.txt')
        self.message = "Test\n"

    def test_add_line(self):
        self.cut.add_line(self.message)
        last_line = self.cut.get_last_line()
        self.assertTrue("Test" in last_line)

    def test_get_lines_count(self):
        lines = self.cut.get_lines_count()
        self.cut.add_line(self.message)
        self.assertEqual(self.cut.get_lines_count(), lines + 1)
