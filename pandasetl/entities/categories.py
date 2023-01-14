class ExtractCategories:
    """Extracts values from data frame 'categories'."""

    def __init__(self, row):
        """
            Assigning the single row from data frame categories to every method.
        """
        self.row = row
       
    def get_category_name(self):
        """
            Takes in one row with category name from categories table and returns it.
        """
        return(self.row.categoryName)
    
    def get_category_id(self):
        """Takes in one row with category id from categories table and returns it."""
        return(self.row.categoryID)
    
    def get_description(self):
        """Takes in one row with description from categories table and returns it."""
        return(self.row.description)
    
    def get_picture(self):
        """Takes in one row with picture from categories table and returns it."""
        return(self.row.picture)
        
        
           
            
        