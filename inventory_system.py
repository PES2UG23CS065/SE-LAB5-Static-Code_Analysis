import json
import logging
from datetime import datetime
import ast

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """
    Adds an item and quantity to the stock.
    Returns True if added successfully, False otherwise.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid input types for add_item: item=%s, qty=%s", item, qty)
        return False

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s to stock", qty, item)
    return True


def remove_item(item, qty):
    """
    Removes a quantity of an item from stock.
    Returns True if removed successfully, False otherwise.
    """
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid input types for remove_item: item=%s, qty=%s", item, qty)
        return False

    try:
        if item not in stock_data:
            logging.warning("Item '%s' not found in stock", item)
            return False

        stock_data[item] -= qty
        logging.info("Removed %d of %s from stock", qty, item)

        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Item '%s' removed completely (qty <= 0)", item)
        return True
    except Exception as e:
        logging.error("Error removing item '%s': %s", item, e)
        return False


def get_qty(item):
    """Returns the quantity of a given item in stock."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file safely."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Data loaded successfully from %s", file)
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty stock.", file)
        stock_data = {}
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in %s. Resetting stock.", file)
        stock_data = {}


def save_data(file="inventory.json"):
    """Saves inventory data to a JSON file safely."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Data saved successfully to %s", file)
    except Exception as e:
        logging.error("Failed to save data to %s: %s", file, e)


def print_data():
    """Logs and prints all items currently in stock."""
    logging.info("Generating Items Report")
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Returns a list of items below the specified quantity threshold."""
    result = [item for item, qty in stock_data.items() if qty < threshold]
    logging.info("Low stock items (below %d): %s", threshold, result)
    return result


def main():
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", -2, logs)
    add_item(123, "ten", logs)  # Invalid input test
    remove_item("apple", 3)
    remove_item("orange", 1)
    logging.info("Apple stock: %d", get_qty("apple"))
    logging.info("Low items: %s", check_low_items())
    save_data()
    load_data()
    print_data()

    # Safe alternative to eval using ast.literal_eval
    safe_expr = "{'message': 'eval replaced safely'}"
    result = ast.literal_eval(safe_expr)
    logging.info("Literal eval result: %s", result)


if __name__ == "__main__":
    main()
