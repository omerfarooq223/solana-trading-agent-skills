import unittest
from decimal import Decimal
from calculate_risk import calculate_position_size_and_risk_reward

class TestRiskManager(unittest.TestCase):
    def test_basic(self):
        result = calculate_position_size_and_risk_reward(10000, 105, 100)
        self.assertIsInstance(result, dict)
        self.assertAlmostEqual(result['position_size_sol'], 2.0, places=2)
        self.assertAlmostEqual(result['dollar_amount_at_risk'], 100.0, places=2)

if __name__ == "__main__":
    unittest.main()
