class Order_details:
    def __init__(self,row):
        self.row = row
        
    def get_order_id(self):
        return(self.row.orderID)
    
    def get_product_id(self):
        return(self.row.productID)
    
    def get_unit_price(self):
        return(self.row.unitPrice)
    
    def get_quantity(self):
        return(self.row.quantity)
    
    def get_discount(self):
        return(self.row.discount)