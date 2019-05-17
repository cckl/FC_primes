import unittest

from primes import MultiplicationTable, is_prime, get_n_primes

class MultiplicationTableTests(unittest.TestCase):
    """Tests for the MultiplicationTable class."""

    def setUp(self):
        self.table = MultiplicationTable()

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            self.table.create_primes_table(-2)
        with self.assertRaises(ValueError):
            self.table.create_primes_table('a')

    def test_n_is_zero(self):
        self.assertEqual(self.table.create_primes_table(0), '0 primes')

    def test_first_row_and_column(self):
        self.table.create_primes_table(10)
        self.assertEqual(self.table.table[0][1], self.table.table[1][0])
        self.assertEqual(self.table.table[0][5], self.table.table[5][0])
        self.assertEqual(self.table.table[0][10], self.table.table[10][0])

    def test_correct_products(self):
        self.table.create_primes_table(10)
        self.assertEqual(self.table.table[1][1], 4)
        self.assertEqual(self.table.table[10][10], 841)

    def test_primes_table_string_spaces(self):
        result = self.table.format_primes_table(10)
        self.assertEqual(result[1], '\t')
        self.assertEqual(result[9], '\t')

    def test_primes_table_string_newlines(self):
        result = self.table.format_primes_table(10)
        self.assertEqual(result[28], '\n')

    def test_primes_table_string_new_row(self):
        result = self.table.format_primes_table(10)
        self.assertEqual(result[29], '2')


class PrimeTests(unittest.TestCase):
    """Tests for prime number functions."""

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(10))

    def test_get_n_primes(self):
        self.assertEqual(get_n_primes(10), [' ', 2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(get_n_primes(2), [' ', 2, 3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
