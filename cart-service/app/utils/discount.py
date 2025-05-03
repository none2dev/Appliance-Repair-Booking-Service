from datetime import datetime
from app.models.discount import DiscountType

def calculate_discounted_price(base_price: float, discount: dict):
    if discount["discount_type"] == DiscountType.FLAT:
        return max(0, base_price - discount["value"])
    elif discount["discount_type"] == DiscountType.PERCENTAGE:
        return base_price * (1 - discount["value"] / 100)
    elif discount["discount_type"] == DiscountType.OFF_PEAK:
        # Off-peak discount logic (e.g., 10% discount during certain hours)
        now = datetime.now().time()
        if discount.get("start_time") and discount.get("end_time"):
            if discount["start_time"] <= now <= discount["end_time"]:
                return base_price * (1 - discount["value"] / 100)
        return base_price
    return base_price