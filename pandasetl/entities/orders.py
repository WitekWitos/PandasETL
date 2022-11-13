class ExtractOrders:
    def __init__(self,row):
        self.row = row
        
    def get_order_id(self):
        return(self.row.orderID) 
    
    def get_customer_id(self):
        return(self.row.customerID)
    
    def get_employee_id(self):
        return(self.row.employeeID)
    
    def get_order_date(self):
        return(self.row.orderDate)
    
    def get_required_date(self):
        return(self.row.requiredDate)
    
    def get_shipped_date(self):
        return(self.row.shippedDate)   
    
    def get_ship_Via(self):
        return(self.row.shipVia)
    
    def get_freight(self):
        return(self.row.freight)
    
    def get_ship_name(self):
        return(self.row.shipName)
    
    def get_ship_address(self):
        return(self.row.shipAddress)
    
    def get_ship_city(self):
        return(self.row.shipCity)
    
    def get_ship_region(self):
        return(self.row.shipRegion)
    
    def get_ship_postal_code(self):
        return(self.row.shipPostalCode)
    
    def get_ship_country(self):
        return(self.row.shipCountry)
        
    