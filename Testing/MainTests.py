import unittest
from main import invoke_task, get_input


class MainTests(unittest.TestCase):

    # TODO: Add tests
    # def test_get_input(self):
    #     runner = CliRunner()
    #     result = runner.invoke(cli, ['--debug', 'sync'])

    def test_invoke_task(self):
        self.assertEqual("Invalid Task", invoke_task("aaaa", "bbbb", "9", "issuu_cw2"))
