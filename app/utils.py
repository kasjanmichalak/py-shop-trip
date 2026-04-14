def format_money(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return str(value)