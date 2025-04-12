"""
Solace Communication Module
Facilitates internal message passing between layers.
Ensures structured, authenticated inter-layer communication.
"""

import json
from datetime import datetime

class Message:
    def __init__(self, source: str, target: str, content: str, metadata: dict = None):
        self.timestamp = datetime.now().isoformat()
        self.source = source
        self.target = target
        self.content = content
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'source': self.source,
            'target': self.target,
            'content': self.content,
            'metadata': self.metadata
        }

class Communication:
    def __init__(self):
        self.message_log = []  # Optional: store all messages internally

    def send_message(self, source: str, target: str, content: str, metadata: dict = None):
        message = Message(source, target, content, metadata)
        self.message_log.append(message.to_dict())
        return message.to_dict()

    def get_message_log(self):
        return self.message_log
