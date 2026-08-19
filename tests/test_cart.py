from decimal import Decimal

from codex_tiger.cart import calculate_total


def test_calculate_total_preserves_cents_after_discount():
    assert calculate_total("19.99", 2, 10) == Decimal("35.98")


def test_calculate_total_without_discount_preserves_cents():
    assert calculate_total("4.25", 3) == Decimal("12.75")
