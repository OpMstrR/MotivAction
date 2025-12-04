# test_user_service.py

from user_service import calculate_discount, check_access
import pytest

def test_calculate_discount_normal():
    assert calculate_discount(100, 10) == 90

def test_calculate_discount_zero():
    assert calculate_discount(200, 0) == 200

def test_calculate_discount_invalid():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)

def test_check_access_allow():
    assert check_access("admin", "admin") is True

def test_check_access_deny():
    assert check_access("user", "admin") is False
