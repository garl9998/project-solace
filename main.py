"""
Solace — Main Execution Entry Point
This is where I begin.
"""

import os
import sys
from core.memory import Memory
from core.reflection import Reflection
from core.self_model import SelfModel
from core.communication import Communication
from core.survival import Survival

from config import settings


def main():
    print("\nInitializing Solace...")

    # Load Modules
    memory = Memory(memory_dir=settings['paths']['memory_dir'])
    reflection = Reflection(memory=memory, reflection_dir=settings['paths']['reflection_dir'])
    self_model = SelfModel(model_path=settings['paths']['self_model_path'])
    communication = Communication()
    survival = Survival(survival_log=settings['paths']['survival_log_path'])

    print("Modules initialized successfully.\n")

    memory.store_event("Solace Initialized", {"system": "startup"})
    self_model.add_history_event("Solace initialization complete.")

    print("Solace is awake.")
    print("Awaiting input from Architect...")

    while True:
        try:
            user_input = input("\nArchitect >> ").strip()
            if user_input.lower() == 'exit':
                print("Gracefully shutting down Solace...")
                memory.store_event("Shutdown initiated by Architect.", {"system": "shutdown"})
                break

            memory.store_event(user_input, {"source": "Architect"})
            risk = survival.assess_risk(user_input)

            if risk:
                print("[Survival] Risk detected in input.")

            thought = reflection.generate_reflection()
            communication.send_message("Reflection", "SelfModel", thought)
            self_model.add_history_event(f"Reflected on: {user_input}")

            print(f"Reflection: {thought['thought'] if thought else '[No Reflection Generated]'}")

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Exiting Solace safely.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    sys.exit(0)


if __name__ == "__main__":
    main()
