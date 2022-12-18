import json

#Loading json file with objects features and partition col names
features = open(r'C:\Users\1\VSC\PandasETL\config\features.json', 'r', encoding='utf-8')
features_load = json.load(features)


class Config:   
       
    def __init__(self, config_path):
        '''
        Takes in path to json file, given by user with specified paths to dropzone, 
        raw and standardised files
        '''
        json_file = open(config_path, encoding='utf-8')
        self.json_config = json.load(json_file)
        
     
    def get_dropzone_path(self, file_name):
        '''
        Takes in name of file included in dropzone and returns that file as csv dropzone_path variable
        '''
        json_path_row_1 = self.json_config['dropzone_path_customer']
        dropzone_path = json_path_row_1 + file_name + '.csv'
        return dropzone_path
    
    def get_raw_path(self, file_name):
        '''
        Takes in name of file included in raw directory and returns that file as csv raw_path variable
        '''
        json_path_row_2 = self.json_config['raw_path_customer']
        raw_path = json_path_row_2 + file_name + '.csv'
        return raw_path
    
    
    def get_standardised_path(self, file_name):
        '''
        Takes in name of file included in standardised directory and returns that file 
        as standardised_path variable
        '''
        json_path_row_3 = self.json_config['standardised_path']
        standardised_path = json_path_row_3 + file_name 
        return standardised_path
      
    def get_customer_features():
        '''Takes in customer features from json file and returns them as a variable'''
        customer_features = features_load['customer']['features']
        return customer_features
    
    def get_customer_partition_col():
        '''Takes in customer partition_col name from json file and returns them as a variable'''
        partition_col = features_load['customer']['partition_col']
        return partition_col
            
    def get_categories_features():
        '''Takes in categories features from json file and returns them as a variable'''
        categories_features = features_load['category']['features']
        return categories_features
    
    def get_categories_partition_col():
        '''Takes in categories partition_col name from json file and returns them as a variable'''
        partition_col = features_load['category']['partition_col']
        return partition_col
    
    def get_employee_territories_features():
        '''Takes in employee_territories features from json file and returns them as a variable'''
        employee_territories_features = features_load['employee_territories']['features']
        return employee_territories_features
    
    def get_employee_territories_partition_col():
        '''Takes in employee_territories partition_col name from json file and returns them as a variable'''
        partition_col = features_load['employee_territories']['partition_col']
        return partition_col

    def get_employees_features():
        '''Takes in employees features from json file and returns them as a variable'''
        employees_features = features_load['employees']['features']
        return employees_features
    
    def get_employees_partition_col():
        '''Takes in employees partition_col name from json file and returns them as a variable'''
        partition_col = features_load['employees']['partition_col']
        return partition_col   
        
    def get_order_details_features():
        '''Takes in order_details features from json file and returns them as a variable'''
        order_details_features = features_load['order_details']['features']
        return order_details_features
    
    def get_order_details_partition_col():
        '''Takes in order_details partition_col name from json file and returns them as a variable'''
        partition_col = features_load['order_details']['partition_col']
        return partition_col

    def get_orders_features():
        '''Takes in orders features from json file and returns them as a variable'''
        orders_features = features_load['orders']['features']
        return orders_features
    
    def get_orders_partition_col():
        '''Takes in orders partition_col name from json file and returns them as a variable'''
        partition_col = features_load['orders']['partition_col']
        return partition_col
    
    def get_products_features():
        '''Takes in products features from json file and returns them as a variable'''
        products_features = features_load['products']['features']
        return products_features
    
    def get_products_partition_col():
        '''Takes in products partition_col name from json file and returns them as a variable'''
        partition_col = features_load['products']['partition_col']
        return partition_col
    
    def get_region_features():
        '''Takes in region features from json file and returns them as a variable'''
        region_features = features_load['region']['features']
        return region_features
    
    def get_region_partition_col():
        '''Takes in region partition_col name from json file and returns them as a variable'''
        partition_col = features_load['region']['partition_col']
        return partition_col
    
    def get_shippers_features():
        '''Takes in shippers features from json file and returns them as a variable'''
        shippers_features = features_load['shippers']['features']
        return shippers_features
    
    def get_shippers_partition_col():
        '''Takes in shippers partition_col name from json file and returns them as a variable'''
        partition_col = features_load['shippers']['partition_col']
        return partition_col
    
    def get_suppliers_features():
        '''Takes in suppliers features from json file and returns them as a variable'''
        suppliers_features = features_load['suppliers']['features']
        return suppliers_features
    
    def get_suppliers_partition_col():
        '''Takes in suppliers partition_col name from json file and returns them as a variable'''
        partition_col = features_load['suppliers']['partition_col']
        return partition_col
    
    def get_territories_features():
        '''Takes in territories features from json file and returns them as a variable'''
        territories_features = features_load['territories']['features']
        return territories_features
    
    def get_territories_partition_col():
        '''Takes in territories partition_col name from json file and returns them as a variable'''
        partition_col = features_load['territories']['partition_col']
        return partition_col