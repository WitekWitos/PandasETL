class ExtractEmployees:
    def __init__(self,row):
        self.row = row
        
    def get_employee_ID(self):
        return(self.row.employeeID)
    
    def get_last_name(self):
        return(self.row.lastName)
    
    def get_first_name(self):
        return(self.row.firstName)
    
    def get_title(self):
        return(self.row.title)
    
    def get_title_of_courtesy(self):
        return(self.row.titleOfCourtesy)
    
    def get_birth_date(self):
        return(self.row.birthDate)
    
    def get_hire_date(self):
        return(self.row.hireDate)
    
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
    
    def get_home_phone(self):
        return(self.row.homePhone)
    
    def get_extension(self):
        return(self.row.extension)
    
    def get_photo(self):
        return(self.row.photo)
    
    def get_notes(self):
        return(self.row.notes)
    
    def get_reports_To(self):
        return(self.row.reportsTo)
    
    def get_photo_path(self):
        return(self.row.photoPath)
    
 