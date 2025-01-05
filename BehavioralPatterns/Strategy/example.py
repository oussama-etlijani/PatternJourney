from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """Abstract base class for a payment strategy."""

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    """Concrete strategy for credit card payment."""

    def __init__(self, card_number, card_holder, expiry_date, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        return f"Paid {amount} using Credit Card: {self.card_number[-4:]}"


class PayPalPayment(PaymentStrategy):
    """Concrete strategy for PayPal payment."""

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount} using PayPal: {self.email}"


class GooglePayPayment(PaymentStrategy):
    """Concrete strategy for Google Pay payment."""

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def pay(self, amount):
        return f"Paid {amount} using Google Pay: {self.phone_number}"


class PaymentProcessor:
    """Context class that uses a payment strategy."""

    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        return self.payment_strategy.pay(amount)


# Example usage
if __name__ == "__main__":
    # Initialize with a Credit Card payment strategy
    credit_card = CreditCardPayment("1234123412341234", "John Doe", "12/25", "123")
    payment_processor = PaymentProcessor(credit_card)
    print(payment_processor.process_payment(100))

    # Switch to PayPal payment strategy
    paypal = PayPalPayment("johndoe@example.com")
    payment_processor.set_payment_strategy(paypal)
    print(payment_processor.process_payment(200))

    # Switch to Google Pay payment strategy
    google_pay = GooglePayPayment("+1234567890")
    payment_processor.set_payment_strategy(google_pay)
    print(payment_processor.process_payment(300))
