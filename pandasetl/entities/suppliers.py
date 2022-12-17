class ExtractSuppliers:
    """Extracts values from data frame 'suppliers'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame suppliers to every method."""
        self.row = row
        
    def get_supplier_id(self):
        """Takes in one row with supplier_id from df suppliers and returns it."""
        return(self.row.supplierID)
    
    def get_company_name(self):
        """Takes in one row with company_name from df suppliers and returns it."""
        return(self.row.companyName)
    
    def get_contact_name(self):
        """Takes in one row with contact_name from df suppliers and returns it."""
        return(self.row.contactName)
    
    def get_contact_title(self):
        """Takes in one row with contact_title from df suppliers and returns it."""
        return(self.row.contactTitle)
    
    def get_address(self):
        """Takes in one row with address from df suppliers and returns it."""
        return(self.row.address)
    
    def get_city(self):
        """Takes in one row with city from df suppliers and returns it."""
        return(self.row.city)
    
    def get_region(self):
        """Takes in one row with region from df suppliers and returns it."""
        return(self.row.region)
    
    def get_postal_code(self):
        """Takes in one row with postal_code from df suppliers and returns it."""
        return(self.row.postalCode)
    
    def get_country(self):
        """Takes in one row with country from df suppliers and returns it."""
        return(self.row.country)
    
    def get_phone(self):
        """Takes in one row with phone from df suppliers and returns it."""
        return(self.row.phone)
    
    def get_fax(self):
        """Takes in one row with fax from df suppliers and returns it."""
        return(self.row.fax)
    
    def get_home_page(self):
        """Takes in one row with home_page from df suppliers and returns it."""
        return(self.row.homePage)