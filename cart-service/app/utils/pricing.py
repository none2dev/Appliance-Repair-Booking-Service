from app.crud.discount import get_discount_by_code
from app.utils.discount import calculate_discounted_price

async def calculate_final_price(db, service_id: int, quantity: int = 1, discount_code: str = None):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        return None
    
    base_price = service.base_price * quantity
    discount_amount = 0.0
    
    if discount_code:
        discount = get_discount_by_code(db, discount_code)
        if discount and discount.is_active:
            discount_amount = calculate_discounted_price(base_price, discount)
    
    final_price = base_price - discount_amount
    return {
        "base_price": base_price,
        "discount_amount": discount_amount,
        "final_price": final_price
    }