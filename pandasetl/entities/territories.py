class ExtractTerritories:
    """Extracts values from data frame 'territories'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame territories to every method."""
        self.row = row 
        
    def get_territoryID(self):
        """Takes in one row with territoryID from df territories and returns it."""
        return(self.row.territoryID)
    
    def get_territory_description(self):
        """Takes in one row with territory_description from df territories and returns it."""
        return(self.row.territoryDescription)
    
    def get_region_id(self):
        """Takes in one row with region_id from df territories and returns it."""
        return(self.row.regionID)