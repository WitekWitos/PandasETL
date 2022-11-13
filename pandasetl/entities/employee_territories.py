class ExtractEmployee_territories:
    def __init__(self,row):
        self.row = row

    def get_employee_ID(self):
        return(self.row.employeeID)
    
    def get_territory_ID(self):
        return(self.row.territoryID)
    