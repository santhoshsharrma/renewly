# Renewly

A terminal-first subscription management system built in Python, focused on persistence, renewal intelligence, and incremental product evolution.

---

## Overview

Renewly is a menu-driven CLI application that helps users manage recurring subscriptions directly from the terminal.  
It allows users to add, view, update, and delete subscriptions, while providing intelligent insights into upcoming renewals and overall spending.

The project is intentionally designed as a **CLI-first system** to establish strong core logic, data handling, and reliability before evolving into a web-based application.

---

## Current Features

- Add new subscriptions with name, cost, and renewal date
- Input validation for numeric amounts and date formats
- Persistent storage using local JSON (data survives app restarts)
- View subscriptions sorted by nearest renewal date
- Automatic calculation of days remaining until renewal
- Update existing subscription details
- Delete subscriptions
- **Subscription Insights**:
  - Total number of subscriptions
  - Total monthly spending
  - Most expensive subscription
- Clean, colorized terminal interface
- Cross-platform terminal support (Windows / Linux / macOS)

---

## Tech Stack

- **Language:** Python 3  
- **Standard Libraries:** `datetime`, `os`, `time`, `json`  
- **Interface:** Terminal (menu-driven CLI)

No external dependencies are required.

---

## How It Works

Renewly runs as an interactive terminal application.  
Users interact through a menu-driven interface to manage subscriptions and view insights.

```bash
python renewly.py
```

## Project Structure
```
renewly/
├── renewly.py        # Core CLI application logic
├── subscriptions.json # Local persistent storage (auto-generated)
├── README.md         # Project documentation
├── .gitignore        # Python ignores
└── LICENSE           # MIT License
```
## License

This project is licensed under the MIT License. See the LICENSE file for details.
