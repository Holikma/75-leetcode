import best_time_to_buy_stock
import unittest


class Test_Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(best_time_to_buy_stock.maxProfit([7,1,5,3,6,4]), 5)

    def test_2(self):
        self.assertEqual(best_time_to_buy_stock.maxProfit([7,6,4,3,1]), 0)

if __name__ == '__main__':
    unittest.main()
