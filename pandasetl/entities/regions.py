class ExtractRegions:
    """Extracts values from data frame 'regions'."""
    
    def __init__(self,row):
        """Assigning the single row from data frame regions to every method."""
        self.row = row
        
    def get_region_id(self):
        """Takes in one row with region_id from df regions and returns it."""
        return(self.row.regionID)
    
    def get_region_description(self):
        """Takes in one row with region_description from df regions and returns it."""
        return(self.row.regionDescription)