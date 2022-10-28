# Ma czytać scieżki z json i zwracać wartość ścieżki
# np. get_dropzone_path
import pandas as pd

json_config = pd.read_json(r'C:\Users\1\VSC\PandasETL\config\filesystem_config.json',orient = 'index')
json_path_row_1 = json_config.iloc[0].iloc[0]
json_path_row_2 = json_config.iloc[1].iloc[0]
json_path_row_3 = json_config.iloc[2].iloc[0]


class Config:
    def __init__(self,file_name):
        self.file_name = file_name
        
        
    def get_dropzone_path(self):
        dropzone_path = json_path_row_1+self.file_name+'.csv'
        return dropzone_path
    
    def get_raw_path(self):
        raw_path = json_path_row_2+self.file_name+'.csv'
        return raw_path
    
    def get_standarised_path(self):
        standarised_path = json_path_row_3+self.file_name+'.csv'
        return standarised_path
      
    
        
        
        

        
        
    