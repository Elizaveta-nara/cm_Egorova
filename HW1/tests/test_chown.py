import unittest
from unittest.mock import patch
from commands import CommandHandler
from filesystem import FileSystem

class TestChownCommand(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem('test.tar')
        self.command_handler = CommandHandler(self.fs)

    @patch('builtins.print')
    def test_chown_valid(self, mock_print):
        result = self.command_handler.chown(['user', '/file1'])
        self.assertEqual(result, "Владелец файла '/file1' изменен на 'user'")

    @patch('builtins.print')
    def test_chown_invalid(self, mock_print):
        result = self.command_handler.chown([])
        self.assertEqual(result, "Использование: chown <новый_владелец> <файл>")