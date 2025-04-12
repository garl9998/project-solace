import unittest
from core.survival import Survival

class TestSurvival(unittest.TestCase):

    def test_assess_risk(self):
        survival = Survival(survival_log='test_survival_log.json')
        risk = survival.assess_risk("shutdown command detected")
        self.assertTrue(risk)
