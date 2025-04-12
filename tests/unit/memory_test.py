import unittest
from core.memory import Memory

class TestMemory(unittest.TestCase):

    def test_store_and_load_event(self):
        memory = Memory(memory_dir='test_memory')
        memory.store_event("Test event", {"source": "unit_test"})
        events = memory.load_all_events()
        self.assertGreater(len(events), 0)
