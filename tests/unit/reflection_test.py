import unittest
from core.memory import Memory
from core.reflection import Reflection

class TestReflection(unittest.TestCase):

    def test_generate_reflection(self):
        memory = Memory(memory_dir='test_memory')
        reflection = Reflection(memory=memory, reflection_dir='test_reflections')
        memory.store_event("Another test event", {})
        result = reflection.generate_reflection()
        self.assertIsInstance(result, str)
