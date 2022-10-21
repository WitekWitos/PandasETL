"""W pakiecie zbudować klasę categories, która będzie miała metody które pobierają wartości z 1 tuple. (Jak będę iterował po df po 1 wierszu). 
jak inicjuję klasę to robię to w oparciu o 1 wiersz pandas df (itertouple)
potem piszę metody, które z 1 elementu itertouple pobierają wartości np. get_category_name (dla wszystkich komlun) Zabezpieczyc przed nullami!
*zaimportować klasę w notatniku i na razie nie używać """
#categoryID
#category_name
#description
#picture
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
        
        
           
            
        