import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class ATMGUI:
    def __init__(self, root):
        self.atm = ATM()
        self.root = root
        self.root.title("ATM SIMULATOR")
        self.root.configure(bg="lightblue")
        self.root.geometry("400x300")

        
        self.title_font = tkfont.Font(family="Arial", size=18, weight="bold")
        self.label_font = tkfont.Font(family="Arial", size=12)
        self.button_font = tkfont.Font(family="Arial", size=10, weight="bold")

        
        self.balance_label = tk.Label(root, text="Balance: $0.00", font=self.label_font, bg="lightblue")
        self.balance_label.pack(pady=10)

        
        self.deposit_frame = tk.Frame(root, bg="lightblue")
        self.deposit_frame.pack(pady=10)
        self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Amount: ", font=self.label_font, bg="lightblue")
        self.deposit_label.pack(side=tk.LEFT)
        self.deposit_entry = tk.Entry(self.deposit_frame, font=self.label_font)
        self.deposit_entry.pack(side=tk.LEFT)
        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", font=self.button_font, bg="green", fg="white", command=self.deposit)
        self.deposit_button.pack(side=tk.LEFT, padx=5)

       
        self.withdraw_frame = tk.Frame(root, bg="lightblue")
        self.withdraw_frame.pack(pady=10)
        self.withdraw_label = tk.Label(self.withdraw_frame, text="Withdraw Amount: ", font=self.label_font, bg="lightblue")
        self.withdraw_label.pack(side=tk.LEFT)
        self.withdraw_entry = tk.Entry(self.withdraw_frame, font=self.label_font)
        self.withdraw_entry.pack(side=tk.LEFT)
        self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw", font=self.button_font, bg="red", fg="white", command=self.withdraw)
        self.withdraw_button.pack(side=tk.LEFT, padx=5)

        
        self.check_balance_button = tk.Button(root, text="Check Balance", font=self.button_font, bg="black", fg="white", command=self.check_balance)
        self.check_balance_button.pack(pady=10)

    def deposit(self):
        amount = self.deposit_entry.get()
        try:
            amount = float(amount)
            if self.atm.deposit(amount):
                messagebox.showinfo("Success", "Deposit successful!")
                self.deposit_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Invalid deposit amount.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
        self.update_balance_label()

    def withdraw(self):
        amount = self.withdraw_entry.get()
        try:
            amount = float(amount)
            if self.atm.withdraw(amount):
                messagebox.showinfo("Success", "Withdrawal successful!")
                self.withdraw_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Invalid or insufficient funds for withdrawal.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
        self.update_balance_label()

    def check_balance(self):
        balance = self.atm.check_balance()
        messagebox.showinfo("Balance", f"Your current balance is: ${balance:.2f}")

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.atm.check_balance():.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()
