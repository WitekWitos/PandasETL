class ExtractEmployee_territories:
    """Extracts values from data frame 'employee_territories'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame employee_territories to every method."""
        self.row = row

    def get_employee_ID(self):
        """Takes in one row with employee_id from employee_territories table and returns it."""
        return(self.row.employeeID)
    
    def get_territory_ID(self):
        """Takes in one row with territory_id from employee_territories table and returns it."""
        return(self.row.territoryID)
    