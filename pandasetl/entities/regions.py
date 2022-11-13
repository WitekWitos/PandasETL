class ExtractRegions:
    def __init__(self,row):
        self.row = row
        
    def get_region_id(self):
        return(self.row.regionID)
    
    def get_region_description(self):
        return(self.row.regionDescription)