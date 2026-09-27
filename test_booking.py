from datetime import date


def validate_booking_dates(start_date, end_date):
    return start_date <= end_date


def test_valid_booking_dates():
    assert validate_booking_dates(date(2026, 10, 1), date(2026, 10, 5)) is True


def test_invalid_booking_dates():
    assert validate_booking_dates(date(2026, 10, 5), date(2026, 10, 1)) is False
