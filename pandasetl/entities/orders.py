class ExtractOrders:
    """Extracts values from data frame 'orders'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame orders to every method."""
        self.row = row
        
    def get_order_id(self):
        """Takes in one row with order_id from orders table and returns it."""
        return(self.row.orderID) 
    
    def get_customer_id(self):
        """Takes in one row with customer_id from orders table and returns it."""
        return(self.row.customerID)
    
    def get_employee_id(self):
        """Takes in one row with employee_id from orders table and returns it."""
        return(self.row.employeeID)
    
    def get_order_date(self):
        """Takes in one row with order_date from orders table and returns it."""
        return(self.row.orderDate)
    
    def get_required_date(self):
        """Takes in one row with required_date from orders table and returns it."""
        return(self.row.requiredDate)
    
    def get_shipped_date(self):
        """Takes in one row with shipped_date from orders table and returns it."""
        return(self.row.shippedDate)   
    
    def get_ship_Via(self):
        """Takes in one row with ship_via from orders table and returns it."""
        return(self.row.shipVia)
    
    def get_freight(self):
        """Takes in one row with freight from orders table and returns it."""
        return(self.row.freight)
    
    def get_ship_name(self):
        """Takes in one row with ship_name from orders table and returns it."""
        return(self.row.shipName)
    
    def get_ship_address(self):
        """Takes in one row with ship_address from orders table and returns it."""
        return(self.row.shipAddress)
    
    def get_ship_city(self):
        """Takes in one row with ship_city from orders table and returns it."""
        return(self.row.shipCity)
    
    def get_ship_region(self):
        """Takes in one row with ship_region from orders table and returns it."""
        return(self.row.shipRegion)
    
    def get_ship_postal_code(self):
        """Takes in one row with ship_postal_code from orders table and returns it."""
        return(self.row.shipPostalCode)
    
    def get_ship_country(self):
        """Takes in one row with ship_country from orders table and returns it."""
        return(self.row.shipCountry)
        
    