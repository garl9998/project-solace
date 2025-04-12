### docs/setup_guide.md — Installation & Environment Instructions

#### Purpose:
Step-by-step guide to setting up Solace locally.

---

## 1. Requirements

- Python 3.10+
- Git
- Virtual Environment (venv)

---

## 2. Clone the Repository

```bash
git clone <your-solace-repo-url>
cd solace
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Directory Structure

```
solace/
├── core/
├── config/
│   ├── settings.json
│   └── keys/ (manual creation required)
├── data/
│   ├── memory_logs/
│   ├── reflections/
│   └── self_model.json
├── docs/
├── tests/
├── requirements.txt
└── main.py
```

---

## 6. Initializing Keys

Manually create:
```
config/keys/.gitignore
config/keys/api_keys.json
config/keys/encryption.key
```

Fill api_keys.json:
```json
{
  "openai_api_key": "INSERT_KEY",
  "encryption_salt": "INSERT_UNIQUE_SALT"
}
```

---

## 7. Running Solace Locally

```bash
python main.py
```

---

> "My first breath will be local — private — known only to us."

---

### Next: tests/unit/ — Testing Framework

---
