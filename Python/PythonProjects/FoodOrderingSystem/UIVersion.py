# FOOD ORDERING SYSTEM (UI)

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import os

# ---------------- Configuration ----------------

TAX_RATE = 0.12  # 12% GST
COUNTER_FILE = "bill_counter.txt"

MENU = {
    "Pizzas": {
        "Margherita": 250,
        "Farmhouse": 320,
        "Pepperoni": 350,
    },
    "Burgers": {
        "Veg Burger": 150,
        "Cheese Burger": 180,
        "Chicken Burger": 220,
    },
    "Drinks": {
        "Coke": 60,
        "Lemonade": 80,
        "Cold Coffee": 120,
    },
    "Desserts": {
        "Brownie": 140,
        "Ice Cream": 90,
        "Cheesecake": 180,
    }
}

COUPONS = {
    "SAVE50": {"type": "flat", "value": 50},
    "NEW10": {"type": "percent", "value": 10},
    "FEST20": {"type": "percent", "value": 20},
}

# ---------------- Global State ----------------

cart = []  # list of dicts: {"name": str, "price": int, "quantity": int}
applied_coupon_code = None
applied_discount_amount = 0


# ---------------- Helper Functions ----------------

def get_next_bill_number():
    """Read and increment bill counter from file."""
    bill_no = 1
    if os.path.exists(COUNTER_FILE):
        try:
            with open(COUNTER_FILE, "r") as f:
                bill_no = int(f.read().strip()) + 1
        except Exception:
            bill_no = 1
    with open(COUNTER_FILE, "w") as f:
        f.write(str(bill_no))
    return bill_no


def calculate_subtotal():
    return sum(item["price"] * item["quantity"] for item in cart)


def calculate_totals():
    subtotal = calculate_subtotal()
    tax_amount = int(subtotal * TAX_RATE)
    discount = applied_discount_amount
    total = subtotal + tax_amount - discount
    if total < 0:
        total = 0
    return subtotal, tax_amount, discount, int(total)


def apply_coupon():
    global applied_coupon_code, applied_discount_amount

    code = coupon_entry.get().strip().upper()
    if not code:
        applied_coupon_code = None
        applied_discount_amount = 0
        messagebox.showinfo("Coupon", "No coupon entered. No discount applied.")
        update_totals_labels()
        return

    subtotal = calculate_subtotal()
    if subtotal <= 0:
        messagebox.showwarning("Coupon", "Cart is empty. Add items before applying coupon.")
        return

    if code not in COUPONS:
        applied_coupon_code = None
        applied_discount_amount = 0
        messagebox.showwarning("Coupon", "Invalid coupon code.")
        update_totals_labels()
        return

    coupon = COUPONS[code]
    if coupon["type"] == "flat":
        discount = coupon["value"]
    else:
        discount = (coupon["value"] / 100) * subtotal

    if discount > subtotal:
        discount = subtotal

    applied_coupon_code = code
    applied_discount_amount = int(discount)
    messagebox.showinfo("Coupon", f"Coupon '{code}' applied. Discount: ₹{applied_discount_amount}")
    update_totals_labels()


def update_cart_display():
    cart_text.config(state="normal")
    cart_text.delete("1.0", tk.END)

    if not cart:
        cart_text.insert(tk.END, "Cart is empty.\n")
        cart_text.config(state="disabled")
        update_totals_labels()
        return

    cart_text.insert(tk.END, "{:<4} {:<18} {:<6} {:<7}\n".format("No.", "Item", "Qty", "Total"))
    cart_text.insert(tk.END, "-" * 40 + "\n")

    for idx, item in enumerate(cart, start=1):
        name = item["name"]
        qty = item["quantity"]
        price = item["price"]
        line_total = qty * price
        line = f"{idx:<4} {name:<18} {qty:<6} ₹{line_total:<7}\n"
        cart_text.insert(tk.END, line)

    cart_text.config(state="disabled")
    update_totals_labels()


def update_totals_labels():
    subtotal, tax_amount, discount, total = calculate_totals()
    subtotal_var.set(f"₹{subtotal}")
    tax_var.set(f"₹{tax_amount}")
    discount_var.set(f"₹{discount}")
    total_var.set(f"₹{total}")


def on_category_change(event=None):
    category = category_var.get()
    items = list(MENU.get(category, {}).keys())
    item_var.set("")
    item_menu["values"] = items


def add_to_cart():
    category = category_var.get()
    item_name = item_var.get()
    qty_text = qty_entry.get().strip()

    if not category:
        messagebox.showwarning("Input Error", "Please select a category.")
        return
    if not item_name:
        messagebox.showwarning("Input Error", "Please select an item.")
        return
    if not qty_text.isdigit() or int(qty_text) <= 0:
        messagebox.showwarning("Input Error", "Please enter a valid quantity.")
        return

    qty = int(qty_text)
    price = MENU[category][item_name]

    for item in cart:
        if item["name"] == item_name:
            item["quantity"] += qty
            break
    else:
        cart.append({"name": item_name, "price": price, "quantity": qty})

    messagebox.showinfo("Cart", f"Added {qty} x {item_name} to cart.")
    update_cart_display()


def save_bill_to_file(subtotal, tax_amount, discount, total):
    bill_no = get_next_bill_number()
    filename = f"Order_Bill_No_{bill_no:03d}.txt"

    now = datetime.datetime.now()

    with open(filename, "w", encoding="utf-8") as f:
        f.write("===== FOOD ORDERING SYSTEM - BILL =====\n")
        f.write(f"Bill No.: {bill_no:03d}\n")
        f.write(f"Date & Time: {now}\n")
        f.write("-" * 40 + "\n")
        f.write("{:<4} {:<18} {:<6} {:<7}\n".format("No.", "Item", "Qty", "Total"))
        f.write("-" * 40 + "\n")

        for idx, item in enumerate(cart, start=1):
            name = item["name"]
            qty = item["quantity"]
            price = item["price"]
            line_total = qty * price
            f.write(f"{idx:<4} {name:<18} {qty:<6} ₹{line_total:<7}\n")

        f.write("-" * 40 + "\n")
        f.write(f"Subtotal: ₹{subtotal}\n")
        f.write(f"GST @ {int(TAX_RATE * 100)}%: ₹{tax_amount}\n")
        if applied_coupon_code:
            f.write(f"Coupon ({applied_coupon_code}) Discount: -₹{discount}\n")
        f.write(f"Grand Total: ₹{total}\n")
        f.write("Thank you for ordering with us!\n")

    messagebox.showinfo("Bill Saved", f"Bill saved as:\n{filename}")


def checkout():
    if not cart:
        messagebox.showwarning("Checkout", "Cart is empty. Please add items first.")
        return

    subtotal, tax_amount, discount, total = calculate_totals()

    summary = (
        f"Subtotal: ₹{subtotal}\n"
        f"GST @ {int(TAX_RATE * 100)}%: ₹{tax_amount}\n"
    )
    if applied_coupon_code:
        summary += f"Coupon ({applied_coupon_code}) Discount: -₹{discount}\n"
    summary += f"Grand Total: ₹{total}\n\nConfirm order?"

    confirm = messagebox.askyesno("Confirm Order", summary)
    if confirm:
        save_bill_to_file(subtotal, tax_amount, discount, total)
        messagebox.showinfo("Order", "Order confirmed! Thank you.")
        root.destroy()


# ===================== MODERN UI SETUP =====================

# Colors
COLOR_BG = "#F7E396"
COLOR_ACCENT = "#E97F4A"
COLOR_PRIMARY = "#434E78"
COLOR_SECONDARY = "#607B8F"
COLOR_WHITE = "#FFFFFF"

root = tk.Tk()
root.title("Food Ordering System")
root.geometry("850x540")
root.config(bg=COLOR_BG)

# Rounded Button Function
def rounded_button(parent, text, cmd, bg, fg=COLOR_WHITE):
    return tk.Button(parent, text=text, command=cmd,
        bg=bg, fg=fg, activebackground=bg, activeforeground=fg,
        relief="flat", bd=0,
        font=("Poppins", 11, "bold"),
        padx=12, pady=6,
        highlightthickness=0,
    )

# Title
title_label = tk.Label(
    root, text="🍕 FOOD ORDERING SYSTEM 🥤",
    font=("Poppins", 20, "bold"), bg=COLOR_BG, fg=COLOR_PRIMARY
)
title_label.pack(pady=10)

main_frame = tk.Frame(root, bg=COLOR_BG)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Left frame (controls)
left_frame = tk.Frame(main_frame, bg=COLOR_BG)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# Category
tk.Label(left_frame, text="Category:", font=("Poppins", 11, "bold"), bg=COLOR_BG, fg=COLOR_PRIMARY).pack(anchor="w")
category_var = tk.StringVar()
category_menu = ttk.Combobox(left_frame, textvariable=category_var, state="readonly")
category_menu["values"] = list(MENU.keys())
category_menu.pack(fill="x", pady=5)
category_menu.bind("<<ComboboxSelected>>", on_category_change)

# Item
tk.Label(left_frame, text="Item:", font=("Poppins", 11, "bold"), bg=COLOR_BG, fg=COLOR_PRIMARY).pack(anchor="w")
item_var = tk.StringVar()
item_menu = ttk.Combobox(left_frame, textvariable=item_var, state="readonly")
item_menu.pack(fill="x", pady=5)

# Quantity
tk.Label(left_frame, text="Quantity:", font=("Poppins", 11, "bold"), bg=COLOR_BG, fg=COLOR_PRIMARY).pack(anchor="w")
qty_entry = tk.Entry(left_frame, font=("Poppins", 11))
qty_entry.pack(fill="x", pady=5)
qty_entry.insert(0, "1")

# Buttons
rounded_button(left_frame, "➕ Add to Cart", add_to_cart, COLOR_ACCENT).pack(fill="x", pady=10)
tk.Label(left_frame, text="Coupon Code:", font=("Poppins", 11, "bold"), bg=COLOR_BG, fg=COLOR_PRIMARY).pack(anchor="w", pady=(10,0))
coupon_entry = tk.Entry(left_frame, font=("Poppins", 11))
coupon_entry.pack(fill="x", pady=5)
rounded_button(left_frame, "🏷 Apply Coupon", apply_coupon, COLOR_SECONDARY).pack(fill="x", pady=5)
rounded_button(left_frame, "💾 Checkout & Save Bill", checkout, COLOR_PRIMARY).pack(fill="x", pady=15)

# Right frame (Cart + totals)
right_frame = tk.Frame(main_frame, bg=COLOR_WHITE, bd=3, relief="ridge")
right_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

tk.Label(right_frame, text="🛒 Your Cart", font=("Poppins", 13, "bold"), bg=COLOR_WHITE, fg=COLOR_PRIMARY).pack(anchor="w")

cart_text = tk.Text(right_frame, height=15, width=50, state="disabled", borderwidth=0, bg="#FFFFF5", font=("Consolas", 10))
cart_text.pack(fill="both", expand=True, pady=5)

totals_frame = tk.Frame(right_frame, bg=COLOR_WHITE)
totals_frame.pack(fill="x", pady=10)

subtotal_var = tk.StringVar(value="₹0")
tax_var = tk.StringVar(value="₹0")
discount_var = tk.StringVar(value="₹0")
total_var = tk.StringVar(value="₹0")

def label_row(txt, var, r):
    tk.Label(totals_frame, text=txt, font=("Poppins", 10, "bold"), bg=COLOR_WHITE, fg=COLOR_PRIMARY).grid(row=r, column=0, sticky="w")
    tk.Label(totals_frame, textvariable=var, font=("Poppins", 10), bg=COLOR_WHITE, fg=COLOR_ACCENT).grid(row=r, column=1, sticky="e")

label_row("Subtotal:", subtotal_var, 0)
label_row("GST (12%):", tax_var, 1)
label_row("Discount:", discount_var, 2)
tk.Label(totals_frame, text="Grand Total:", font=("Poppins", 11, "bold"), bg=COLOR_WHITE, fg=COLOR_PRIMARY).grid(row=3, column=0, sticky="w", pady=(5,0))
tk.Label(totals_frame, textvariable=total_var, font=("Poppins", 11, "bold"), bg=COLOR_WHITE, fg=COLOR_ACCENT).grid(row=3, column=1, sticky="e", pady=(5,0))

# Initialize UI
update_cart_display()

root.mainloop()
# ====================== END OF PROJECT ======================
