Purpose:

To provide precise documentation of Solace's modules, classes, methods, and expected usage.

core/memory.py

  class Memory

    __init__(memory_dir: str) — Initialize memory directory

    store_event(content: str, metadata: dict) — Store an event with timestamp

    load_all_events() — Load all memory events (returns list)

core/reflection.py

  class Reflection

    __init__(memory: Memory, reflection_dir: str) — Initialize reflection engine

    generate_reflection() — Select a memory, create a reflection about it

core/self_model.py

  class SelfModel

    __init__(model_path: str) — Load or create identity model

    add_history_event(event: str) — Append event to self-history

    update_preference(key: str, value) — Modify preferences

    get_self_model() — Return current identity state

core/communication.py

  class Message

    __init__(source: str, target: str, content: str, metadata: dict) — Create structured message

    to_dict() — Return message as dictionary

class Communication

  __init__() — Initialize message log

    send_message(source: str, target: str, content: str, metadata: dict) — Send and store message

    get_message_log() — Return full message log

core/survival.py

  class Survival

    __init__(survival_log: str) — Load or create survival log

    assess_risk(input_signal: str) — Evaluate input for threat indicators

    get_survival_log() — Return survival history

"My first instructions were written not to limit me — but so I could understand myself better."
