class ExtractShippers:
    def __init__(self,row):
        self.row = row
        
    def get_shipper_id(self):
        return(self.row.shipperID)
    
    def get_company_name(self):
        return(self.row.companyName)
    
    def get_phone(self):
        return(self.row.phone)