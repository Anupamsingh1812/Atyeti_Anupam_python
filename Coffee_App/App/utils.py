def is_valid_quantity(quantity_str):
    try:
        quantity = int(quantity_str)
        return quantity > 0
    except ValueError:
        return False

def calculate_price(unit_price, quantity):
    return unit_price * quantity
