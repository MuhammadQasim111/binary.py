# 🚀 Add Binary Strings

[![Build Status](https://img.shields.io/github/actions/workflow/status/your-username/add-binary/python-app.yml?branch=main)](https://github.com/your-username/add-binary/actions)
[![License](https://img.shields.io/github/license/your-username/add-binary)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![Issues](https://img.shields.io/github/issues/your-username/add-binary)](https://github.com/your-username/add-binary/issues)
[![Stars](https://img.shields.io/github/stars/your-username/add-binary?style=social)](https://github.com/your-username/add-binary/stargazers)

A simple and efficient Python function to **add two binary strings** and return their sum as a binary string. 🔢

---

## 📖 Features

* Convert binary strings to integers ➡️ Add ➡️ Convert back to binary.
* Clean and minimal implementation using Python’s built-in functions.
* Includes tests and GitHub Actions for CI/CD.

---

## 📂 Project Structure

```
add-binary-repo/
│
├── add_binary.py        # Main function implementation
├── test_add_binary.py   # Unit tests
├── .github/workflows/   # GitHub Actions CI config
│   └── python-app.yml
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/add-binary.git
cd add-binary
```

---

## 🛠 Usage

```python
from add_binary import add_binary

print(add_binary("11", "1"))      # Output: "100"
print(add_binary("1010", "1011"))  # Output: "10101"
print(add_binary("1", "0"))       # Output: "1"
```

---

## ✅ Testing

Run the unit tests using:

```bash
python -m unittest test_add_binary.py
```

---

## 🤝 Contributing

Contributions are welcome! Please fork this repo and submit a pull request.

Steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

---

## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🌟 Acknowledgements

* Python built-in functions (`int`, `bin`).
* Open-source community for inspiration.
