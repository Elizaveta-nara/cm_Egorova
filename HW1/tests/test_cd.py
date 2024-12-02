import unittest
from commands import CommandHandler
from filesystem import FileSystem

class TestCdCommand(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem('test.tar')
        self.command_handler = CommandHandler(self.fs)

    def test_cd_root(self):
        result = self.command_handler.cd(['/'])
        self.assertEqual(result, '')

    def test_cd_relative(self):
        result = self.command_handler.cd(['dir'])
        self.assertEqual(result, '')