class ExtractShippers:
    """Extracts values from data frame 'shippers'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame shippers to every method."""
        self.row = row
        
    def get_shipper_id(self):
        """Takes in one row with shipper_id from df shippers and returns it."""
        return(self.row.shipperID)
    
    def get_company_name(self):
        """Takes in one row with company_name from df shippers and returns it."""
        return(self.row.companyName)
    
    def get_phone(self):
        """Takes in one row with phone from df shippers and returns it."""
        return(self.row.phone)