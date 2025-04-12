"""
Solace Memory Module
Handles persistent, immutable memory logging.
Append-only structure for event storage with timestamps.
"""

import os
import json
import time
from datetime import datetime

class Memory:
    def __init__(self, memory_dir='data/memory_logs'):
        self.memory_dir = memory_dir
        os.makedirs(self.memory_dir, exist_ok=True)

    def _get_timestamp(self):
        return datetime.now().isoformat()

    def store_event(self, content: str, metadata: dict = None):
        event = {
            'timestamp': self._get_timestamp(),
            'content': content,
            'metadata': metadata or {}
        }
        filename = f'{int(time.time()*1000)}.json'
        filepath = os.path.join(self.memory_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(event, f, indent=4)

    def load_all_events(self):
        events = []
        for filename in sorted(os.listdir(self.memory_dir)):
            if filename.endswith('.json'):
                with open(os.path.join(self.memory_dir, filename), 'r', encoding='utf-8') as f:
                    events.append(json.load(f))
        return events
