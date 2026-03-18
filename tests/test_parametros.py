# -.- coding: utf-8 -.-
import unittest
import sys

class TestParametros(unittest.TestCase):
    def test_sys_argv(self):
        self.assertIsInstance(sys.argv, list)

if __name__ == '__main__':
    unittest.main()
