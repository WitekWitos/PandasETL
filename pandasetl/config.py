import pandas as pd



class Config:
    def __init__(self, config_path):
        '''
        Opis klasy
        '''
        self.json_config = pd.read_json(config_path, orient = 'index')
        
     
    def get_dropzone_path(self, file_name):
        '''
        Opis metody (co wchodzi do metody, co robi metoda, co wychodzi z metody, dla wszystkich metod)
        '''
        json_path_row_1 = self.json_config.iloc[0].iloc[0]
        dropzone_path = json_path_row_1 + file_name + '.csv'
        return dropzone_path
    
    def get_raw_path(self, file_name):
        json_path_row_2 = self.json_config.iloc[1].iloc[0]
        raw_path = json_path_row_2 + file_name + '.csv'
        return raw_path
    
    def get_standardised_path(self, file_name):
        json_path_row_3 = self.json_config.iloc[2].iloc[0]
        standardised_path = json_path_row_3 + file_name + '.parquet'
        return standardised_path
      
    
        
        
        

        
        
    