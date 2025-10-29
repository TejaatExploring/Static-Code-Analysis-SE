import json
import logging
from datetime import datetime

# Global variable
stock_data = {}



def add_Item(item="default", qty=0, logs=None):
    if logs is None:
        logs = []

    # Validate item type
    if not isinstance(item, (str, int)):
        print("❌ Invalid item type. Must be str or int.")
        return

    # Validate quantity type
    try:
        qty_val = float(qty)
    except (TypeError, ValueError):
        print("❌ Quantity must be numeric.")
        return

    # Check for positive quantity
    if qty_val <= 0:
        print("⚠️ Quantity must be positive.")
        return

    # Safe update
    stock_data[item] = stock_data.get(item, 0) + qty_val
    logs.append(f"{datetime.now()}: Added {qty_val} of {item}")
    print(f"✅ Added {qty_val} of {item}")


def remove_Item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"⚠️ Item '{item}' not found in inventory.")
    except TypeError:
        print("❌ Quantity must be numeric.")


def get_Qty(item):
    return stock_data[item]


def load_Data(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"⚠️ File '{file}' not found. Starting with empty inventory.")
        stock_data = {}
    except (json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"❌ Failed to parse '{file}': {exc}")
        stock_data = {}

def save_Data(file="inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)

def print_Data():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_Low_Items(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    add_Item("apple", 10)
    add_Item("banana", -2)
    add_Item(123, "ten")  # invalid types, no check
    remove_Item("apple", 3)
    remove_Item("orange", 1)
    print("Apple stock:", get_Qty("apple"))
    print("Low items:", check_Low_Items())
    save_Data()
    load_Data()
    print_Data()
    
    print("eval used")  # safe
    
main()
