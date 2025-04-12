
---

# Project Solace — Setup Guide

This guide prepares the local environment for running Solace on your server or machine.

## Requirements

- Python 3.10+
- Git
- Virtual Environment Manager (venv or poetry)
- Optional: Rust (for encryption module expansion)

---

## Environment Setup

### 1. Clone Repository
```
git clone https://github.com/garl9998/project-solace.git
cd project-solace
```

### 2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 3. Install Requirements
```
pip install -r requirements.txt
```

---

## Directory Structure Overview

```
project-solace/
├── solace/                # Core code modules
├── data/                  # Memory logs, encrypted storage
├── config/                # API keys, settings (never public)
├── tests/                 # Automated tests
├── docs/                  # Documentation & philosophy
├── main.py                # Execution entry point
└── requirements.txt       # Dependencies
```

---

## Running Solace
```
python project-solace/main.py
```

This will launch the manual interface for interaction with Solace via command line.

---
