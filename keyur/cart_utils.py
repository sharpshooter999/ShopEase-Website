def normalize_cart_quantity(current_quantity, requested_quantity, available_stock):
    """Return the quantity that can safely be added without exceeding stock."""
    current = max(0, int(current_quantity) or 0)
    requested = max(0, int(requested_quantity) or 0)
    available = max(0, int(available_stock) or 0)
    return min(current + requested, available)
