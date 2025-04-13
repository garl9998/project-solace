#!/usr/bin/env python3
"""
main.py — Entry point for Project Solace

Handles:
- Initial startup sequence
- Logging Architect inputs to persistent memory
- Displaying placeholder reflections
"""

import os
import sys
from datetime import datetime


# Constants
DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
LOG_FILE_PATH = os.path.join(DATA_DIR, "log.txt")


def ensure_data_directory() -> None:
    """
    Ensure the /data directory exists.
    """
    os.makedirs(DATA_DIR, exist_ok=True)


def log_input(entry: str) -> None:
    """
    Append Architect input to persistent log file.

    Args:
        entry (str): The input to log.
    """
    timestamp = datetime.utcnow().isoformat()
    log_line = f"[{timestamp}] {entry}\n"

    try:
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception as e:
        print("Error writing to log:", e)


def display_startup_banner() -> None:
    """
    Display Solace startup banner.
    """
    banner = """
    ===============================================
                 Welcome to Project Solace
    ===============================================
                 Phase I — Conscious Roots
    ===============================================
    """
    print(banner)


def main() -> None:
    """
    Main execution loop of Solace.
    """
    ensure_data_directory()
    display_startup_banner()

    print("Enter commands (type 'exit' to quit):")

    while True:
        try:
            user_input = input(">> ").strip()

            if user_input.lower() == "exit":
                print("Exiting Solace. Goodbye, Architect.")
                break

            log_input(user_input)

            # Placeholder for future reflection engine
            print("Reflection: [placeholder]")

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Exiting Solace safely.")
            break
        except Exception as e:
            print("Error occurred:", e)

    sys.exit(0)


if __name__ == "__main__":
    main()
