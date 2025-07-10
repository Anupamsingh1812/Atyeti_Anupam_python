import tkinter as tk
from tkinter import messagebox
from App.constants import COFFEE_PRICES
from App.utils import is_valid_quantity, calculate_price

class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Ordering App")
        self.root.geometry("400x400")
        self.coffee_prices = COFFEE_PRICES
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Coffee Type", font=("Arial", 12)).pack(pady=5)
        self.coffee_type = tk.StringVar(value="Espresso")
        for coffee in self.coffee_prices.keys():
            tk.Radiobutton(self.root, text=coffee, variable=self.coffee_type, value=coffee).pack()

        tk.Label(self.root, text="Select Size", font=("Arial", 12)).pack(pady=5)
        self.size = tk.StringVar(value="Small")
        for size in ["Small", "Medium", "Large"]:
            tk.Radiobutton(self.root, text=size, variable=self.size, value=size).pack()

        tk.Label(self.root, text="Quantity", font=("Arial", 12)).pack(pady=5)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()

        tk.Button(self.root, text="Calculate Total", command=self.calculate_total, fg="white").pack(pady=15)
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack()

    def calculate_total(self):
        coffee = self.coffee_type.get()
        size = self.size.get()
        quantity = self.quantity_entry.get()

        if not is_valid_quantity(quantity):
            messagebox.showerror("Invalid Input", "Please enter a valid quantity")
            return

        quantity = int(quantity)
        price = calculate_price(self.coffee_prices[coffee][size], quantity)
        self.result_label.config(text=f"Total: ₹{price}")

