class ExtractSuppliers:
    def __init__(self,row):
        self.row = row
        
    def get_supplier_id(self):
        return(self.row.supplierID)
    
    def get_company_name(self):
        return(self.row.companyName)
    
    def get_contact_name(self):
        return(self.row.contactName)
    
    def get_contact_title(self):
        return(self.row.contactTitle)
    
    def get_address(self):
        return(self.row.address)
    
    def get_city(self):
        return(self.row.city)
    
    def get_region(self):
        return(self.row.region)
    
    def get_postal_code(self):
        return(self.row.postalCode)
    
    def get_country(self):
        return(self.row.country)
    
    def get_phone(self):
        return(self.row.phone)
    
    def get_fax(self):
        return(self.row.fax)
    
    def get_home_page(self):
        return(self.row.homePage)