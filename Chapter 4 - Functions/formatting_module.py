# Chapter 4: Multiple Modules — Formatting Logic (formatting_module.py)
# ====================================================================
# This module is responsible strictly for text and currency presentation.

def format_currency(amount):
    """Formats a numeric amount into Indian Rupee representation: Rs. X,XXX.XX"""
    return f"Rs. {amount:,.2f}"


def format_header(title, width=45):
    """Generates a clean decorated banner header."""
    border = "=" * width
    centered_title = title.center(width)
    return f"{border}\n{centered_title}\n{border}"


def format_summary_line(label, value_str, width=45):
    """Formats an aligned key-value line for invoices and reports."""
    dots_count = width - len(label) - len(value_str) - 2
    dots = "." * max(dots_count, 1)
    return f"{label} {dots} {value_str}"


if __name__ == "__main__":
    print("--- Testing formatting_module.py standalone ---")
    print(format_header("INVOICE PREVIEW"))
    print(format_summary_line("Subtotal", format_currency(950)))
    print(format_summary_line("Tax (5%)", format_currency(47.50)))
    print(format_summary_line("Final Total", format_currency(997.50)))
