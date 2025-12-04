# user_service.py

def calculate_discount(price, percent):
    if price < 0 or percent < 0:
        raise ValueError("Price and percent must be positive")

    return price - (price * percent / 100)

def check_access(user_role, required_role):
    return user_role == required_role
