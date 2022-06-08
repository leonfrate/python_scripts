import unittest
from main import *


class TestScript(unittest.TestCase):

    def test_db_connection(self):
        self.assertTrue(connection1.is_connected())
        self.assertTrue(connection2.is_connected())

    def test_variable_types(self):
        self.assertIsNotNone(query1)


if __name__ == '__main__':
    unittest.main()
