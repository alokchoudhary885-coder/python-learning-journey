# Chapter 4: Working with Multiple Modules
# Demonstrates coordinating business logic and formatting across multiple files.

import arithmetic_module as calc
import formatting_module as fmt


def generate_invoice(customer_name, items):
    print(fmt.format_header(f"INVOICE: {customer_name.upper()}"))
    subtotal = 0.0

    for name, qty, price in items:
        item_total = qty * price
        subtotal += item_total
        line_desc = f"{name} (x{qty})"
        print(fmt.format_summary_line(line_desc, fmt.format_currency(item_total)))

    # Calculation logic handled by arithmetic_module
    pricing = calc.compute_final_price(subtotal, discount_percent=10, tax_rate=0.05)

    print("-" * 45)
    print(fmt.format_summary_line("Subtotal", fmt.format_currency(pricing["base_price"])))
    print(fmt.format_summary_line("Discount (10%)", f"- {fmt.format_currency(pricing['discount'])}"))
    print(fmt.format_summary_line("Tax (5%)", f"+ {fmt.format_currency(pricing['tax'])}"))
    print("=" * 45)
    print(fmt.format_summary_line("Amount Payable", fmt.format_currency(pricing["final_total"])))


if __name__ == "__main__":
    order_items = [
        ("Python Book", 2, 450.0),
        ("Spiral Notebook", 3, 80.0),
        ("Gel Pen Pack", 1, 120.0),
    ]

    generate_invoice("Alok Choudhary", order_items)
