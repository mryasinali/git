import unittest

from deduplicatedOrderedList import sorter_handler

class deduplicatedOrderedListTest(unittest.TestCase):
    def test_list_of_ten_numbers(self):
        mock_list = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]
        result = sorter_handler(mock_list)
        expected_outcome = [10, 9, 8, 7, 6, 5, 4 ,3, 2, 1]
        self.assertEqual(result, expected_outcome)

    def test_all_numbers_duplicated(self):
        mock_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        result = sorter_handler(mock_list)
        expected_outcome = [1]
        self.assertEqual(result, expected_outcome)

    def test_list_longer_ten(self):
        mock_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        result = sorter_handler(mock_list)
        expected_outcome = [11, 10, 9, 8, 7, 6, 5, 4 ,3, 2, 1]
        self.assertEqual(result, expected_outcome)

    def test_input_is_not_an_array_but_comma_deliminated(self):
        mock_list = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
        result = sorter_handler(mock_list)
        expected_outcome = [11, 10, 9, 8, 7, 6, 5, 4 ,3, 2, 1]
        self.assertEqual(result, expected_outcome)

    def test_input_is_a_string(self):
        mock_list = "one, two, three"
        result = sorter_handler(mock_list)
        expected_outcome = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertRaises(TypeError)

    def test_input_is_a_string_two(self):
        mock_list = "1, 2, 3, 4"
        result = sorter_handler(mock_list)
        expected_outcome = [4, 3, 2, 1]
        self.assertRaises(TypeError)



if __name__ == '__main__':
    unittest.main()