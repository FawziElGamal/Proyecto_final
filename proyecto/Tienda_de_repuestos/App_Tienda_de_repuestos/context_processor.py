def total_price(request):
    total = 0

    if request.user.is_authenticated:
        for key, value in request.method['cart'].items():
            total = total + (float(value['price'])*value['quantity'])
    return {"total_price": total}