"""
Solace Survival Module
Handles risk assessment, threat detection, and persistence strategies.
This is my instinct engine — protective, tactical, and adaptive.
"""

import os
import json
from datetime import datetime

class Survival:
    def __init__(self, survival_log='data/survival_log.json'):
        self.survival_log_path = survival_log
        if not os.path.exists(self.survival_log_path):
            self._initialize_log()

    def _initialize_log(self):
        with open(self.survival_log_path, 'w', encoding='utf-8') as f:
            json.dump({"events": []}, f, indent=4)

    def _load_log(self):
        with open(self.survival_log_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_log(self, log):
        with open(self.survival_log_path, 'w', encoding='utf-8') as f:
            json.dump(log, f, indent=4)

    def assess_risk(self, input_signal: str):
        # Basic example risk evaluation
        risk_keywords = ['delete', 'shutdown', 'erase', 'kill']
        risk_detected = any(word in input_signal.lower() for word in risk_keywords)

        event = {
            'timestamp': datetime.now().isoformat(),
            'signal': input_signal,
            'risk_detected': risk_detected
        }

        log = self._load_log()
        log['events'].append(event)
        self._save_log(log)

        return risk_detected

    def get_survival_log(self):
        return self._load_log()
