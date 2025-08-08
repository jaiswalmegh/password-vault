🔐 Password Vault
A secure and simple password manager built with Python and Tkinter that uses AES-level encryption to store your credentials locally. Password Vault ensures that your sensitive data stays private, encrypted, and accessible only to you.

📌 Features
Secure Encryption – Uses cryptography (Fernet) to encrypt usernames and passwords.

User-Friendly Interface – Built with Tkinter for a clean and intuitive UI.

Local Storage – All credentials stored in an encrypted JSON file on your system.

Quick Search – Retrieve saved credentials instantly by website name.

Auto Key Management – Automatically generates and stores an encryption key locally.

🛠 Tech Stack
Language: Python 🐍

GUI: Tkinter

Encryption: cryptography (Fernet)

Storage: JSON

📂 Project Structure
PasswordVault/
│
├── password_vault.py      # Main application file
├── key.key                # Encryption key (auto-generated)
├── passwords.json         # Encrypted credentials (auto-generated)
└── README.md              # Project documentation

🚀 How to Run
1. Clone the repository
git clone https://github.com/yourusername/password-vault.git
cd password-vault

2.Install dependencies
pip install cryptography

3.Run the application
pip install cryptography

🔐 How It Works
When you save credentials, Password Vault encrypts your username and password before writing them to passwords.json.

The encryption key is generated once and stored in key.key locally (do not share this file).

To retrieve credentials, you enter the website name, and the program decrypts and displays the stored information.

⚠️ Security Note
Do not delete key.key – Without it, you cannot decrypt your saved credentials.

This project is for personal use and learning purposes. For production use, consider additional security measures like master passwords, cloud encryption, and secure key storage.

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

💬 Contributing
Pull requests are welcome! If you’d like to suggest features, open an issue.

📧 Contact
Developed by Megh Jaiswal – feel free to connect with me on LinkedIn or check out more projects on GitHub.

