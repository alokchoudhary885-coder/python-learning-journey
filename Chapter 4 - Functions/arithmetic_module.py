# Chapter 4: Multiple Modules — Math Logic (arithmetic_module.py)
# ==============================================================
# This module is responsible strictly for calculation logic (Separation of Concerns).

def calculate_discount(price, discount_percent):
    """Calculates discount amount from price and percentage."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100.")
    return (price * discount_percent) / 100


def calculate_tax(amount, tax_rate=0.05):
    """Calculates tax on an amount based on tax_rate (default 5%)."""
    return amount * tax_rate


def compute_final_price(base_price, discount_percent=0.0, tax_rate=0.05):
    """
    Computes final price after applying discount and adding tax.
    Formula: (base_price - discount) + tax
    """
    discount = calculate_discount(base_price, discount_percent)
    subtotal = base_price - discount
    tax = calculate_tax(subtotal, tax_rate)
    final_total = subtotal + tax
    return {
        "base_price": base_price,
        "discount": discount,
        "subtotal": subtotal,
        "tax": tax,
        "final_total": final_total,
    }


if __name__ == "__main__":
    print("--- Testing arithmetic_module.py standalone ---")
    result = compute_final_price(1000, discount_percent=10, tax_rate=0.05)
    print("Final price dict:", result)
