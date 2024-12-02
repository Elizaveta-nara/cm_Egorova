import unittest
from unittest.mock import patch
from commands import CommandHandler
from filesystem import FileSystem

class TestTacCommand(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem('test.tar')
        self.command_handler = CommandHandler(self.fs)

    @patch('builtins.print')
    def test_tac_valid(self, mock_print):
        result = self.command_handler.tac(['/file1'])
        self.assertIn("line3", result)

    @patch('builtins.print')
    def test_tac_invalid(self, mock_print):
        result = self.command_handler.tac([])
        self.assertEqual(result, "Не указан файл")