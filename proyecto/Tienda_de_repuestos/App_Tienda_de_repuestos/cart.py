class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        # cart = self.session("cart")
        cart = self.session.get("cart")


        if not cart:
            cart = self.session["cart"] = {}

        # else:
        self.cart = cart

    def add_item(self, product):
        if (str(product.part_number) not in self.cart.keys()):
            self.cart[product.part_number] = {
                "part_number": product.part_number,
                "description": product.description,
                "price": product.price_usd,
                "quantity": 1,
                "image": product.image.url
            }
        else:
            for key, value in self.cart.items():
                if key==str(product.part_number):
                    value["quantity"] = value["quantity"] + 1
                    break

        self.save_cart()
    
    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def erase_product(self, product):
        product.part_number = str(product.part_number)
        if product.part_number in self.cart:
            del self.cart[product.part_number]
            self.save_cart()

    def subtract_product(self, product):
        for key, value in self.cart.items():
            if key==str(product.part_number):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.erase_product(product)
                break    
        self.save_cart()

    def clear_chart(self):
        self.session["cart"] = {}
        self.session.modified = True