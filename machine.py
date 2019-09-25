
class Machine(object):
    """docstring for Machine"""
    def __init__(self):
        """docstring for init"""
        self.products = {
        "A" : {
            "description": "Chocolate biscuits",
            "price": 100,
            "stock": 10
            }
        }

        self.inserted_money = 0

    def insert_money(self, coins):
        for coin, value in coins.items():
            self.inserted_money += coin * value

    def press_button(self, code):
        if self.inserted_money < self.products[code]["price"] or self.products[code]["stock"] == 0 :
            return (None,None)

        self.inserted_money -= self.products[code]["price"]
        self.products[code]["stock"] -= 1
        return (code,self.inserted_money)

    def press_cancel(self):
        amount = self.inserted_money
        self.inserted_money=0
        return amount

