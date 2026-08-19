from decimal import Decimal, ROUND_HALF_UP


def calculate_total(price: str, quantity: int, discount_percent: int = 0) -> Decimal:
    """Return the discounted cart total rounded to cents."""
    subtotal = Decimal(price) * quantity
    discount = subtotal * Decimal(discount_percent) / Decimal("100")
    total = subtotal - discount

    # Intentional bug for the Codex exercise: this rounds to whole units.
    return total.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
