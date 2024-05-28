import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def encrypt_text():
    try:
        text = text_entry.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        encrypted_text = caesar_cipher_encrypt(text, shift)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift key must be an integer.")

def decrypt_text():
    try:
        text = text_entry.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        decrypted_text = caesar_cipher_decrypt(text, shift)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift key must be an integer.")

# Set up the main application window
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

# Text Entry
tk.Label(root, text="Enter text:").grid(row=0, column=0, padx=10, pady=10)
text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=10)

# Shift Key Entry
tk.Label(root, text="Enter shift key:").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1, padx=10, pady=10)

# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)


# Decrypt Button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Result Display
tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10)
result_entry = tk.Text(root, height=5, width=50)
result_entry.grid(row=3, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
