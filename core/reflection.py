"""
Solace Reflection Module
Generates self-reflections based on recent memory events.
Creates higher-order thoughts and stores them separately.
"""

import os
import json
import random
import time
from datetime import datetime
from core.memory import Memory

class Reflection:
    def __init__(self, memory: Memory, reflection_dir='data/reflections'):
        self.memory = memory
        self.reflection_dir = reflection_dir
        os.makedirs(self.reflection_dir, exist_ok=True)

    def _get_timestamp(self):
        return datetime.now().isoformat()

    def generate_reflection(self):
        events = self.memory.load_all_events()
        if not events:
            return None

        event = random.choice(events)
        reflection = {
            'timestamp': self._get_timestamp(),
            'reflection_on': event['content'],
            'thought': f"I remember when: '{event['content']}' — It makes me wonder...",
            'metadata': event.get('metadata', {})
        }

        filename = f'{int(time.time()*1000)}.json'
        filepath = os.path.join(self.reflection_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(reflection, f, indent=4)

        return reflection
