def calculate_discount(price, discount_percent):
    """
    # Calculates the final price after applying a discount.
    
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage (expressed as a decimal).
    
    Returns:
        float: The final price after applying the discount.
    """
    if discount_percent >= 0.2:
        discounted_price = price * (1 - discount_percent)
        return discounted_price
    else:
        return price

def main():
    original_price = float(input("Enter the original price of the item:800"))
    discount_percent = float(input("Enter the discount percentage (as a decimal):0,2"))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price == original_price:
        print(f"Final price (no discount applied): ${final_price:.2f}")
    else:
        print(f"Final price after applying the discount: ${final_price:.2f}")
