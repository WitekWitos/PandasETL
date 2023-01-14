from pandasetl.entities.employees import ExtractEmployees
from pandasetl.config import Config
import pandas as pd


employees_features = Config.get_employees_features()
partition_col = Config.get_employees_partition_col()

class PipelineEmployees:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractEmployees(row)
            result.append((df_row.get_employee_ID(), df_row.get_last_name(), df_row.get_first_name(), 
                           df_row.get_title(), df_row.get_title_of_courtesy(), df_row.get_birth_date(), 
                           df_row.get_hire_date(), df_row.get_address(),df_row.get_city(), df_row.get_region(), 
                           df_row.get_postal_code(), df_row.get_country(), df_row.get_home_phone(),
                           df_row.get_extension(), df_row.get_photo(), df_row.get_notes(), df_row.get_reports_To(), 
                           df_row.get_photo_path()))
        df_transformed = pd.DataFrame(result, columns = employees_features)
        print(df_transformed.head(3))
        return df_transformed