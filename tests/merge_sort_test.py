from random import randint
import unittest
from merge_sort import *


def generate_random_number_list(list_size):
    rand_list = []
    for count in range(list_size):
        rand_list.append(randint(0, list_size*2))
    return rand_list


def is_sorted(a_list):
    for i in range(1, len(a_list)):
        if a_list[i-1] > a_list[i]:
            return False
    return True


class SearchSortTests(unittest.TestCase):

    def test_merge(self):
        self.assertEqual([1, 2, 3, 4], merge([1, 4], [2, 3]))
        self.assertEqual([1, 2, 3, 4], merge([1, 3], [2, 4]))
        self.assertEqual([1, 2, 3, 4], merge([1, 2], [3, 4]))

        self.assertEqual([1, 1, 3, 4, 5, 5, 8], merge([1, 4, 8], [1, 3, 5, 5]))
        self.assertEqual([1, 1, 3, 3, 4, 5, 5, 8], merge([1, 3, 4, 5, 5, 8], [1, 3]))

        self.assertEqual([], merge([], []))
        self.assertEqual([1], merge([1], []))
        self.assertEqual([1], merge([], [1]))
        self.assertEqual([1, 1], merge([1], [1]))
        self.assertEqual([1, 3], merge([3], [1]))

    def test_merge_sort(self):
        self.assertEqual([1, 2, 3, 4, 5], merge_sort([2, 1, 4, 5, 3]))
        self.assertEqual([1, 1, 2, 3, 3, 3, 5, 7], merge_sort([3, 2, 1, 7, 1, 5, 3, 3]))

        rand_list = generate_random_number_list(10000)
        sorted_list = merge_sort(rand_list)
        self.assertNotEqual(rand_list, sorted_list)
        self.assertEqual(len(rand_list), len(sorted_list))
        for num in sorted_list:
            self.assertEqual(rand_list.count(num), sorted_list.count(num))
        self.assertTrue(is_sorted(sorted_list))

