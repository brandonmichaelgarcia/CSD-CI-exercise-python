# -*- coding: utf-8 -*-
import unittest

from sanitizer import sanitize


class SanitizerTest(unittest.TestCase):
    def test_string_sanitizer_removes_spaces(self):
        # Arrange
        expected = "00201485672"
        # Act
        result = sanitize("0 0201485672")
        # Assert
        self.assertEqual(expected, result)

    def test_string_sanitizer_removes_dashes(self):
        # Arrange
        expected = "9780596809485"
        # Act
        result = sanitize("978-0596809485")
        # Assert
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
