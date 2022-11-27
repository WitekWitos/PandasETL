import pandas as pd
import json
# w tej klasie napisać metody do wyciągania rzeczy i używam konkretnej metody do wyciągnięcia 
# konkretnych informacji z json
# przerobić na json.load tak jak w klasach pipelines

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
    
    #usunąć datę i parquet ze standardised
    def get_standardised_path(self, file_name):
        json_path_row_3 = self.json_config.iloc[2].iloc[0]
        standardised_path = json_path_row_3 + file_name + '.parquet'
        return standardised_path
      
    #def get_customer_features():
    # metoda ma zwracać konkretną listę features dla customer
    #pass
        
        
        

        
        
    