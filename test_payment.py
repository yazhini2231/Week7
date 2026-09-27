def validate_payment_amount(amount):
    return isinstance(amount, (int, float)) and amount > 0


def test_valid_payment():
    assert validate_payment_amount(2500) is True


def test_zero_payment():
    assert validate_payment_amount(0) is False


def test_negative_payment():
    assert validate_payment_amount(-100) is False
