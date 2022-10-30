class Territories:
    def __init__(self,row):
        self.row = row 
        
    def get_territoryID(self):
        return(self.row.territoryID)
    
    def get_territory_description(self):
        return(self.row.territoryDescription)
    
    def get_region_id(self):
        return(self.row.regionID)