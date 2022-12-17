class ExtractCustomer:
    """Extracts values from data frame 'customer'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame customer to every method."""
        self.row = row
        
    def get_customer_id(self):
        """Takes in one row with customer_id from customer table and returns it."""
        return(self.row.customerID)
        
    def get_company_name(self):
        """Takes in one row with company_name from customer table and returns it."""
        return(self.row.companyName)         
        
    def get_contact_name(self):
        """Takes in one row with contact_name from customer table and returns it."""
        return(self.row.contactName) 
         
    def get_contact_title(self):
        """Takes in one row with contact_title from customer table and returns it."""
        return(self.row.contactTitle)
    
    def get_address(self):
        """Takes in one row with address from customer table and returns it."""
        return(self.row.address)
    
    def get_city(self):
        """Takes in one row with city from customer table and returns it."""
        return(self.row.city)
    
    def get_region(self):
        """Takes in one row with region from customer table and returns it."""
        return(self.row.region)
    
    def get_postal_code(self):
        """Takes in one row with postal_code from customer table and returns it."""
        return(self.row.postalCode)
    
    def get_coutry(self):
        """Takes in one row with country from customer table and returns it."""
        return(self.row.country)
    
    def get_phone(self):
        """Takes in one row with phone from customer table and returns it."""
        return(self.row.phone)
    
    def get_fax(self):
        """Takes in one row with fax from customer table and returns it."""
        return(self.row.fax)


                                   