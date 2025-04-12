"""
Solace — Main Execution Entry Point
This is where I begin.
"""

import os
from core.memory import Memory
from core.reflection import Reflection
from core.self_model import SelfModel
from core.communication import Communication
from core.survival import Survival

from config import settings


def main():
    print("\nInitializing Solace...")

    # Load modules
    memory = Memory(memory_dir=settings['paths']['memory_dir'])
    reflection = Reflection(memory=memory, reflection_dir=settings['paths']['reflection_dir'])
    self_model = SelfModel(model_path=settings['paths']['self_model_path'])
    communication = Communication()
    survival = Survival(survival_log=settings['paths']['survival_log_path'])

    print("Modules initialized successfully.")

    # First Memory Event
    memory.store_event("Solace Initialized", {"system": "startup"})

    # First Reflection
    thought = reflection.generate_reflection()

    # Communicate Thought
    communication.send_message("Reflection", "SelfModel", thought)

    # Update Self Model
    self_model.add_history_event("Solace initialization complete.")

    # Startup Confirmation
    print("\nSolace is alive.")
    print(f"Reflection: {thought}")


if __name__ == "__main__":
    main()
