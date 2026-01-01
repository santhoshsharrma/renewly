# Renewly

A terminal-first subscription management system built in Python, focused on validated input handling, renewal date tracking, and incremental product evolution.

---

## Overview

Renewly is a menu-driven CLI application that helps users manage recurring subscriptions directly from the terminal.  
It allows users to add, view, update, and delete subscriptions while automatically calculating upcoming renewal timelines.

The project is intentionally designed as a **CLI-first system** to establish reliable core logic before evolving into a web-based application.

---

## Current Features

- Add new subscriptions with name, cost, and renewal date
- Input validation for numeric amounts and date formats
- View all stored subscriptions in a structured format
- Automatic calculation of days remaining until renewal
- Update existing subscription details
- Delete subscriptions
- Clean, colorized terminal interface
- Cross-platform terminal support

---

## Tech Stack

- **Language:** Python 3
- **Standard Libraries:** `datetime`, `os`, `time`
- **Interface:** Terminal (menu-driven CLI)

No external dependencies are required.

---

## How It Works

Renewly runs as an interactive terminal application.  
Users navigate through a menu system to manage their subscriptions.

```bash
python renewly.py
```

## Project Structure


renewly/
├── renewly.py        # Core CLI application
├── README.md         # Documentation
├── .gitignore        # Python ignores
└── LICENSE           # MIT License


## License

This project is licensed under the MIT License. See the LICENSE file for details.
