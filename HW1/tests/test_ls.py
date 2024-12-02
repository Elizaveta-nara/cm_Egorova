import unittest
from unittest.mock import patch
from commands import CommandHandler
from filesystem import FileSystem

class TestLsCommand(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem('test.tar')
        self.command_handler = CommandHandler(self.fs)

    @patch('builtins.print')
    def test_ls_root(self, mock_print):
        result = self.command_handler.ls([])
        self.assertIn('/file1', result)

    @patch('builtins.print')
    def test_ls_directory(self, mock_print):
        result = self.command_handler.ls(['/dir'])
        self.assertIn('/dir/file2', result)