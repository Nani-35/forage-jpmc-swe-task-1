import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self):
    """ Test the getRatio function """
    self.assertEqual(getRatio(10, 2), 5.0)
    self.assertEqual(getRatio(15, 3), 5.0)
    self.assertEqual(getRatio(20, 4), 5.0)
    self.assertEqual(getRatio(0, 5), 0.0)
    self.assertIsNone(getRatio(10, 0))  # Division by zero
    self.assertEqual(getRatio(-10, -2), 5.0)
    self.assertEqual(getRatio(-15, 3), -5.0)
    self.assertEqual(getRatio(10, -2), -5.0)
    self.assertEqual(getRatio(5, 5), 1.0)
    self.assertEqual(getRatio(100, 100), 1.0)
    self.assertEqual(getRatio(1e6, 1e3), 1000.0)
    self.assertEqual(getRatio(1e9, 1e6), 1000.0)
    self.assertEqual(getRatio(1e9, 1e6), 1000.0)




if __name__ == '__main__':
    unittest.main()
