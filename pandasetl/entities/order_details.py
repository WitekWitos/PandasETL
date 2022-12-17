class ExtractOrder_details:
    """Extracts values from data frame 'order_details'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame order_details to every method."""
        self.row = row
        
    def get_order_id(self):
        """Takes in one row with order_id from order_details table and returns it."""
        return(self.row.orderID)
    
    def get_product_id(self):
        """Takes in one row with product_id from order_details table and returns it."""
        return(self.row.productID)
    
    def get_unit_price(self):
        """Takes in one row with unit_price from order_details table and returns it."""
        return(self.row.unitPrice)
    
    def get_quantity(self):
        """Takes in one row with quantity from order_details table and returns it."""
        return(self.row.quantity)
    
    def get_discount(self):
        """Takes in one row with discount from order_details table and returns it."""
        return(self.row.discount)