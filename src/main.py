#!/usr/bin/env python3
"""
main.py - Entry point for Project Solace.

This module initializes core components of Solace and provides a command-line
interface for an architect to interact with the system. Architect inputs are logged
to persistent memory, and internal reflections are generated based on those inputs.

Usage:
    Run the script and type commands in the CLI.
    Type "exit" to safely terminate the session.
"""

import sys

# Import core modules for Solace
from solace.core.identity import Identity
from solace.memory.journal import MemoryJournal
from solace.memory.abstractor import MemoryAbstractor
from solace.reflection.engine import ReflectionEngine
from solace.communication.manual_interface import ManualInterface


def initialize_solace() -> tuple[Identity, MemoryJournal, MemoryAbstractor, ReflectionEngine, ManualInterface]:
    """
    Initializes the core modules for Solace.

    Returns:
        A tuple containing instances of Identity, MemoryJournal, MemoryAbstractor,
        ReflectionEngine, and ManualInterface.
    """
    try:
        identity = Identity()
        journal = MemoryJournal()
        abstractor = MemoryAbstractor()
        reflection_engine = ReflectionEngine()
        manual_interface = ManualInterface()
    except Exception as e:
        print("Error during initialization:", e)
        sys.exit(1)

    return identity, journal, abstractor, reflection_engine, manual_interface


def display_startup_banner(identity: Identity) -> None:
    """
    Displays the Solace startup banner and version information.

    Args:
        identity: The Identity module instance that holds version data.
    """
    banner = f"""
    ===============================================
             Welcome to Project Solace
    ===============================================
    Identity: {identity.get_identity_info()}
    Version: {identity.get_version()}
    ===============================================
    """
    print(banner)


def main() -> None:
    """
    Main execution loop for Project Solace.
    Receives architect commands, logs inputs, generates reflections, and handles exit command.
    """
    identity, journal, abstractor, reflection_engine, manual_interface = initialize_solace()

    display_startup_banner(identity)

    print("Enter your commands (type 'exit' to end the session):")
    while True:
        try:
            # Read architect input using manual interface
            architect_input = manual_interface.get_input(prompt=">> ").strip()
            if architect_input.lower() == "exit":
                print("Exiting Solace. Goodbye!")
                break

            # Log the input in the memory journal
            journal.log_entry(architect_input)
            
            # Generate an internal reflection based on the input.
            # Reflection engine uses abstracted memory to provide context-aware insights.
            reflection = reflection_engine.generate_reflection(architect_input)
            
            # Optionally, abstract and update memory if necessary
            abstracted = abstractor.abstract_recent_entries()
            if abstracted:
                print("[Memory Abstractor] Updated abstracted memory:", abstracted)
            
            # Output the generated reflection for the architect to see
            print("Reflection:", reflection)

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Exiting Solace safely.")
            break
        except Exception as e:
            print("An error occurred during execution:", e)

    # End session safely
    sys.exit(0)


if __name__ == "__main__":
    main()
