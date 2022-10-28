
import pandas as pd
df = pd.read_csv(r'C:\Users\1\Documents\filesystem\dropzone\categories.csv')

class Categories:
    def __init__(self,row:int):
        self.row = df.iloc[row]
        
    def get_category_name(self):
        return(self.row.categoryName)
    
    def get_category_id(self):
        return(self.row.categoryID)
    
    def get_description(self):
        return(self.row.description)
    
    def get_picture(self):
        return(self.row.picture)
        
        
           
            
        