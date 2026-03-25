import unittest
from logger import calculate_pnl, log_trade
import os

class TestTradeLogger(unittest.TestCase):
    def setUp(self):
        self.testfile = 'test_trades.csv'
        # Remove file if exists
        if os.path.exists(self.testfile):
            os.remove(self.testfile)

    def tearDown(self):
        if os.path.exists(self.testfile):
            os.remove(self.testfile)

    def test_log_and_pnl(self):
        log_trade('buy', 2, 100, filename=self.testfile)
        log_trade('sell', 1, 120, filename=self.testfile)
        pnl = calculate_pnl(filename=self.testfile)
        self.assertEqual(pnl['total_bought'], 2)
        self.assertEqual(pnl['total_sold'], 1)
        self.assertEqual(pnl['remaining_holdings'], 1)
        self.assertAlmostEqual(pnl['pnl'], 20.0, places=2)

if __name__ == "__main__":
    unittest.main()
