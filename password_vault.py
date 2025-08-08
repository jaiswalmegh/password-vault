import tkinter as tk
from tkinter import messagebox
import json
from cryptography.fernet import Fernet
import os

# --- Encryption Setup ---
KEY_FILE = "key.key"
DATA_FILE = "passwords.json"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

key = load_key()
fernet = Fernet(key)

def encrypt(data):
    return fernet.encrypt(data.encode()).decode()

def decrypt(data):
    return fernet.decrypt(data.encode()).decode()

# --- Functionality ---
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    new_data = {
        website: {
            "username": encrypt(username),
            "password": encrypt(password)
        }
    }

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Password saved successfully!")

def retrieve_password():
    website = website_entry.get()
    if not website:
        messagebox.showwarning("Warning", "Enter website to search!")
        return

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        if website in data:
            decrypted_username = decrypt(data[website]["username"])
            decrypted_password = decrypt(data[website]["password"])
            messagebox.showinfo("Found", f"Username: {decrypted_username}\nPassword: {decrypted_password}")
        else:
            messagebox.showerror("Not Found", "No entry found for this website.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved passwords found.")

# --- UI Setup ---
root = tk.Tk()
root.title("🔐 Password Vault")
root.geometry("420x400")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# --- Header ---
header = tk.Label(root, text="🔐 Secure Password Manager", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50", pady=10)
header.pack()

# --- Input Frame ---
frame = tk.Frame(root, bg="#34495e", padx=20, pady=20)
frame.pack(pady=10, padx=20, fill="both", expand=True)

def create_label(text):
    return tk.Label(frame, text=text, fg="white", bg="#34495e", anchor="w", font=("Segoe UI", 10, "bold"))

create_label("🌐 Website:").pack(anchor="w", pady=(0, 5))
website_entry = tk.Entry(frame, width=40, font=("Segoe UI", 10))
website_entry.pack(pady=(0, 10))

create_label("📧 Username/Email:").pack(anchor="w", pady=(0, 5))
username_entry = tk.Entry(frame, width=40, font=("Segoe UI", 10))
username_entry.pack(pady=(0, 10))

create_label("🔑 Password:").pack(anchor="w", pady=(0, 5))
password_entry = tk.Entry(frame, width=40, show="*", font=("Segoe UI", 10))
password_entry.pack(pady=(0, 20))

# --- Buttons ---
btn_style = {"font": ("Segoe UI", 10, "bold"), "padx": 10, "pady": 5, "width": 20}

save_btn = tk.Button(root, text="💾 Save Password", bg="#27ae60", fg="white", command=save_password, **btn_style)
save_btn.pack(pady=5)

retrieve_btn = tk.Button(root, text="🔍 Retrieve Password", bg="#2980b9", fg="white", command=retrieve_password, **btn_style)
retrieve_btn.pack(pady=5)

exit_btn = tk.Button(root, text="❌ Exit", bg="#c0392b", fg="white", command=root.quit, **btn_style)
exit_btn.pack(pady=5)

root.mainloop()
