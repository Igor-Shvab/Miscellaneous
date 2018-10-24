import unittest, sys, os

sys.path.append('../')
from bakery_solution import coins_given

class MyTest(unittest.TestCase):

	# Testing Vegimite Scroll  -  VS5
    # Check for correct batch price
    def test_bakery_batch_price(self):
    	self.assertEqual(coins_given(10, [(8.99,5), (6.99,3)])[0].keys()[0], 8.99)

    # Check for correct batch quantity
    def test_bakery_batch_quantity(self):
    	self.assertEqual(coins_given(10, [(8.99,5), (6.99,3)])[0][8.99], 2)

if __name__ == '__main__':
	unittest.main()
