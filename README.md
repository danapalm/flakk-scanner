# 🕷️ FLAKK - Custom Web Scanner v0.3.6

**FLAKK** is a simple, customizable, and interactive subdomain scanner designed to help you find active subdomains on a target domain.
It features a user-friendly console interface with keyboard navigation (arrow keys) using `InquirerPy` and color highlighting with `colorama` to emphasize important results.

---

## 📦 Features

- Multithreaded scanning of common subdomains
- Interactive menu with arrow key navigation (`InquirerPy`)
- Color support for better readability (`colorama`)
- Console visuals with ASCII art (`pyfiglet`)
- Automatic terminal cleanup
- Option to save scans into text files
- Option to repeat scans or exit easily

---

## 📁 Project Structure

```bash
FLAKK/
├── scripts/
│   └── simple_domains.py        # Module containing the subdomain scanner
│
├── flakk.py                     # Main file that runs the interactive menu
├── README.md                    # Project documentation
├── requirements.txt             # Required dependencies
└── __init__.py                  # (optional, for package recognition. Everything is managed from flakk.py)
```
---

## 🛠️ Requirements

- Python 3.8+
- Python modules (requirements.txt)

---
## 🚀 Installation, Dependencies, and Usage

To clone this project, use the following command:

```bash
git clone https://github.com/danapalm/flakk-scanner.git
```

To install the dependencies:

```bash
pip install -r requirements.txt
```

To run the tool:

```bash
python flakk.py
```


---
## 🧠 Preview

```bash
[*] Scanning domain: example.com

[+] http://www.example.com -> 200
[+] http://mail.example.com -> 403

[!] Found 2 valid subdomains:
 - http://www.example.com
 - http://mail.example.com
```

---
## 📌 Customization

You can edit the list of subdomains in:

```bash
scripts/simple_domains.py
```

Subdomain list:
```bash
SUBDOMAINS = [
    'www', 'mail', 'ftp', 'webmail', 'localhost', 'cpanel', 'api', 'test', 'dev'
]
```

---
## 🧑‍💻 Author

[Check out my github👻](https://github.com/danapalm)
