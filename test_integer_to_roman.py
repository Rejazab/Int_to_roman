import unittest
from integer_to_roman import from_integer_to_roman
import roman

class test_belows_tens(unittest.TestCase):
	def setUp(self):
		"""Call before every test case."""

	def tearDown(self):
		"""Call after every test case."""

	def testBelow5(self):
		for i in range(1,5): 
			assert from_integer_to_roman(i) == roman.toRoman(i), 'Issue with value '+str(i)

	def testSmallExceptions(self):
		assert from_integer_to_roman(4) == 'IV', 'Issue with value 4'
		assert from_integer_to_roman(5) == 'V', 'Issue with value 5'
		assert from_integer_to_roman(9) == 'IX', 'Issue with value 9'

	def testAbove5(self):
		assert from_integer_to_roman(6) == 'VI', 'Issue with value 6'
		assert from_integer_to_roman(8) == 'VIII', 'Issue with value 8'


class test_tens(unittest.TestCase):
	def setUp(self):
		"""Call before every test case."""

	def tearDown(self):
		"""Call after every test case."""

	def testBelow50(self):
		for i in range(10,49):
			assert from_integer_to_roman(i) == roman.toRoman(i), 'Issue with value '+str(i)

	def testTensException(self):
		assert from_integer_to_roman(40) == 'XL', 'Issue with value 40'
		assert from_integer_to_roman(50) == 'L', 'Issue with value 50'
		assert from_integer_to_roman(90) == 'XC', 'Issue with value 90'

	def testAbove50(self):
		for i in range(50,100): assert from_integer_to_roman(i) == roman.toRoman(i), 'Issue with value '+str(i)

class test_hundreds(unittest.TestCase):
	def setUp(self):
		"""Call before every test case."""

	def tearDown(self):
		"""Call after every test case."""

class test_thousands(unittest.TestCase):
	def setUp(self):
		"""Call before every test case."""

	def tearDown(self):
		"""Call after every test case."""


if __name__ == "__main__":
	unittest.main() 