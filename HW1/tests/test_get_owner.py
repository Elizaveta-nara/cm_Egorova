import unittest
from unittest.mock import patch
from commands import CommandHandler
from filesystem import FileSystem

class TestGetOwnerCommand(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem('test.tar')
        self.command_handler = CommandHandler(self.fs)

    @patch('builtins.print')
    def test_get_owner_valid(self, mock_print):
        self.command_handler.chown(['user', '/file1'])
        result = self.command_handler.get_owner(['/file1'])
        self.assertEqual(result, "Владелец файла '/file1': user")

    @patch('builtins.print')
    def test_get_owner_invalid(self, mock_print):
        result = self.command_handler.get_owner([])
        self.assertEqual(result, "Использование: owner <файл>")