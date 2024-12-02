import unittest
from unittest.mock import patch
from commands import CommandHandler
from filesystem import FileSystem

class TestUptimeCommand(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem('test.tar')
        self.command_handler = CommandHandler(self.fs)

    @patch('builtins.print')
    def test_uptime(self, mock_print):
        result = self.command_handler.uptime()
        self.assertIn("Время работы системы:", result)