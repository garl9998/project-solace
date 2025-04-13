
import unittest
from core.communication import Communication


class TestCommunication(unittest.TestCase):

    def test_send_and_retrieve_message(self):
        communication = Communication()

        source = "Memory"
        target = "Reflection"
        content = "Testing message passing"
        metadata = {"importance": "high"}

        message = communication.send_message(source, target, content, metadata)

        self.assertEqual(message['source'], source)
        self.assertEqual(message['target'], target)
        self.assertEqual(message['content'], content)
        self.assertIn('timestamp', message)
        self.assertEqual(message['metadata'], metadata)

        log = communication.get_message_log()
        self.assertGreater(len(log), 0)
        self.assertIn(message, log)


if __name__ == '__main__':
    unittest.main()
