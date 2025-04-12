import unittest
from core.memory import Memory
from core.reflection import Reflection
from core.self_model import SelfModel
from core.communication import Communication
from core.survival import Survival

class TestSystemIntegration(unittest.TestCase):

    def test_full_system_interaction(self):
        memory = Memory(memory_dir='test_memory')
        reflection = Reflection(memory=memory, reflection_dir='test_reflections')
        self_model = SelfModel(model_path='test_self_model.json')
        communication = Communication()
        survival = Survival(survival_log='test_survival_log.json')

        # Store event
        memory.store_event("Integration Test Event", {"source": "integration_test"})

        # Generate Reflection
        thought = reflection.generate_reflection()

        # Communicate Thought
        message = communication.send_message("Reflection", "SelfModel", thought)

        # Update Self Model
        self_model.add_history_event("Integrated Reflection Created")

        # Assess Risk
        risk = survival.assess_risk("This is a harmless string")

        self.assertIsInstance(thought, str)
        self.assertIn("Integrated Reflection Created", self_model.get_self_model()['history'])
        self.assertFalse(risk)
        self.assertGreater(len(communication.get_message_log()), 0)
