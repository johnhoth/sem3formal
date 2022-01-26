import unittest
from library import solve as test_function
import library


class TestLibraryExceptions(unittest.TestCase):

    def test_inapplicable_operand(self):
        self.assertRaises(library.InapplicableOperator, test_function, '.', 'a')

    def test_no_operand(self):
        self.assertRaises(library.NoOperand, test_function, 'aaa.*', 'a')

    def test_unknown_symbol(self):
        self.assertRaises(library.UnknownSymbol, test_function, 'ab.*cd.+', 'a')

    def test_inapplicable_operand_star(self):
        self.assertRaises(library.InapplicableOperator, test_function, '*', 'a')

    def test_inapplicable_operand_plus(self):
        self.assertRaises(library.InapplicableOperator, test_function, 'a+', 'a')


class TestLibrary(unittest.TestCase):

    def test_from_example(self):
        self.assertEqual(test_function('ab+c.aba.*.bac.+.+*', 'a'), 2)

    def test_from_example2(self):
        self.assertEqual(test_function('acb..bab.c.*.ab.ba.+.+*a.', 'a'), 2)

    def test_empty_symbol(self):
        self.assertEqual(test_function('1*aaa..+', 'a'), 3)

    def test_simple_string(self):
        self.assertEqual(test_function('aaaa...', 'a'), 4)

    def test_stars(self):
        self.assertEqual(test_function('a*', 'a'), 'INF')

    def test_concat(self):
        self.assertEqual(test_function('aaa..abb...aa.ab..+', 'a'), 4)

    def test_hard(self):
        self.assertEqual(test_function('ba.a.a.b.aa.b.a.a.+*', 'a'), 4)

    def test_hard2(self):
        self.assertEqual(test_function('aaa.ba.+*1a+ba.+..', 'a'), 'INF')

    def test_hard3(self):
        self.assertEqual(test_function('ccc.*.', 'c'), 'INF')

    def test_hard4(self):
        self.assertEqual(test_function('a1+ab.b+1+*.', 'a'), 2)

    def test_hard5(self):
        self.assertEqual(test_function('b*a1+a1+a1+...', 'a'), 3)

    def test_hard6(self):
        self.assertEqual(test_function('a1+*', 'a'), 'INF')
