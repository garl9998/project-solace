import unittest
from core.self_model import SelfModel

class TestSelfModel(unittest.TestCase):

    def test_add_history_and_get_self(self):
        model = SelfModel(model_path='test_self_model.json')
        model.add_history_event("Created for testing")
        self.assertIn("Created for testing", model.get_self_model()['history'])
