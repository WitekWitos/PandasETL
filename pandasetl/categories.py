
class Categories:
    def __init__(self, row):
        self.row = row
        
    def get_category_name(self):
        return(self.row.categoryName)
    
    def get_category_id(self):
        return(self.row.categoryID)
    
    def get_description(self):
        return(self.row.description)
    
    def get_picture(self):
        return(self.row.picture)
        
        
           
            
        