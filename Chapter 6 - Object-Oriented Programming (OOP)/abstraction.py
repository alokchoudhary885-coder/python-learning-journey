# Chapter 6: Abstraction in Python
# Demonstrates Abstract Base Classes (ABC) and @abstractmethod to enforce interfaces.

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    """Abstract Base Class representing a payment processor contract."""

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def authenticate(self):
        """Must be implemented by subclasses."""
        pass

    @abstractmethod
    def process_payment(self):
        """Must be implemented by subclasses."""
        pass

    def generate_receipt(self):
        """Concrete method shared by all payment gateways."""
        print(f"Receipt generated for transaction of Rs. {self.amount:,.2f}")


class UPIPayment(PaymentGateway):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def authenticate(self):
        print(f"Verifying UPI MPIN for ID: {self.upi_id}")
        return True

    def process_payment(self):
        if self.authenticate():
            print(f"Processing UPI payment of Rs. {self.amount:,.2f} instantly.")
            self.generate_receipt()


class CreditCardPayment(PaymentGateway):
    def __init__(self, amount, card_number, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.cvv = cvv

    def authenticate(self):
        print(f"Validating card ending in {self.card_number[-4:]} with OTP.")
        return True

    def process_payment(self):
        if self.authenticate():
            print(f"Charged credit card Rs. {self.amount:,.2f} via banking gateway.")
            self.generate_receipt()


if __name__ == "__main__":
    print("--- 1. Abstraction in Action ---")
    # Trying to instantiate abstract class raises TypeError
    try:
        gateway = PaymentGateway(500)
    except TypeError as e:
        print("Cannot instantiate abstract class:", e)

    print("\n--- 2. UPI Payment ---")
    upi = UPIPayment(850.0, "alok@okaxis")
    upi.process_payment()

    print("\n--- 3. Credit Card Payment ---")
    card = CreditCardPayment(3200.0, "4532112233445566", "789")
    card.process_payment()
