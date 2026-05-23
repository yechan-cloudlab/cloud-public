import unittest

from src.cost_calculator import estimate_cost, estimate_request_for_model
from src.router import route_request


class CostCalculatorTests(unittest.TestCase):
    def test_estimate_cost_splits_input_and_output_tokens(self):
        self.assertEqual(estimate_cost(1_000_000, 1_000_000, 1.0, 2.0), 3.0)

    def test_estimate_cost_handles_small_token_count(self):
        self.assertEqual(estimate_cost(1_000, 2_000, 1.0, 2.0), 0.005)

    def test_estimate_cost_rejects_negative_tokens(self):
        with self.assertRaisesRegex(ValueError, 'non-negative'):
            estimate_cost(-1, 0, 1.0, 2.0)

    def test_estimate_request_for_model(self):
        pricing = {
            'models': {
                'claude-haiku': {
                    'input_per_1m': 1.0,
                    'output_per_1m': 5.0,
                }
            }
        }
        request = {'input_tokens': 1_000, 'output_tokens': 1_000}
        self.assertEqual(estimate_request_for_model(request, pricing, 'claude-haiku'), 0.006)


class RouterTests(unittest.TestCase):
    def test_route_request_uses_matching_category(self):
        rules = {
            'default_model': 'claude-sonnet',
            'rules': [{'category': 'summarize', 'model': 'claude-haiku'}],
        }
        self.assertEqual(route_request('summarize', rules), 'claude-haiku')

    def test_route_request_falls_back_to_default(self):
        rules = {'default_model': 'claude-sonnet', 'rules': []}
        self.assertEqual(route_request('unknown', rules), 'claude-sonnet')


if __name__ == '__main__':
    unittest.main()
