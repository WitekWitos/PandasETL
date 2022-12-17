class ExtractEmployees:
    """Extracts values from data frame 'employees'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame employees to every method."""
        self.row = row
        
    def get_employee_ID(self):
        """Takes in one row with employee_id from employees table and returns it."""
        return(self.row.employeeID)
    
    def get_last_name(self):
        """Takes in one row with last_name from employees table and returns it."""
        return(self.row.lastName)
    
    def get_first_name(self):
        """Takes in one row with first_name from employees table and returns it."""
        return(self.row.firstName)
    
    def get_title(self):
        """Takes in one row with tittle from employees table and returns it."""
        return(self.row.title)
    
    def get_title_of_courtesy(self):
        """Takes in one row with tittle_of_courtesy from employees table and returns it."""
        return(self.row.titleOfCourtesy)
    
    def get_birth_date(self):
        """Takes in one row with birth_date from employees table and returns it."""
        return(self.row.birthDate)
    
    def get_hire_date(self):
        """Takes in one row with hire_date from employees table and returns it."""
        return(self.row.hireDate)
    
    def get_address(self):
        """Takes in one row with address from employees table and returns it."""
        return(self.row.address)
    
    def get_city(self):
        """Takes in one row with city from employees table and returns it."""
        return(self.row.city)
    
    def get_region(self):
        """Takes in one row with region from employees table and returns it."""
        return(self.row.region)
    
    def get_postal_code(self):
        """Takes in one row with postal_code from employees table and returns it."""
        return(self.row.postalCode)
    
    def get_country(self):
        """Takes in one row with country from employees table and returns it."""
        return(self.row.country)
    
    def get_home_phone(self):
        """Takes in one row with home_phone from employees table and returns it."""
        return(self.row.homePhone)
    
    def get_extension(self):
        """Takes in one row with employee_id from employees table and returns it."""
        return(self.row.extension)
    
    def get_photo(self):
        """Takes in one row with photo from employees table and returns it."""
        return(self.row.photo)
    
    def get_notes(self):
        """Takes in one row with notes from employees table and returns it."""
        return(self.row.notes)
    
    def get_reports_To(self):
        """Takes in one row with repots_to from employees table and returns it."""
        return(self.row.reportsTo)
    
    def get_photo_path(self):
        """Takes in one row with photo_path from employees table and returns it."""
        return(self.row.photoPath)
    
 