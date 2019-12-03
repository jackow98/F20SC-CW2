import unittest
from FileManagement import FileManagement


class FileManagementTests(unittest.TestCase):

    # TODO: Make generic test files for simple, extreme and exceptional data
    # TODO: include tests for all files
    def setUp(self) -> None:
        # Performs this method before every test, use self to define any variables
        self.full_provided_malformed__json = FileManagement("issuu_cw2")
        self.full_provided_correctly_formed_json = FileManagement("issuu_cw2_new")
        self.created_simple_test_data = FileManagement("simple_test")

    def test_load_file(self):
        self.assertEqual(self.full_provided_malformed__json.load_file(), self.full_provided_correctly_formed_json.load_file())

    def test_get_visitors(self):
        self.assertEqual(self.created_simple_test_data.get_visitors("1"), ["a", "b", "c", "d", ])

    def test_get_documents(self):
        self.assertEqual(self.created_simple_test_data.get_documents("a"), {"a": ["1", "4"]})


if __name__ == '__main__':
    test = FileManagementTests()