from pandasetl.entities.employee_territories import ExtractEmployee_territories
import pandas as pd
import json

features_copy = open(r'C:\Users\1\VSC\PandasETL\config\features.json','r', encoding='utf-8')
data = json.load(features_copy)
employee_territories_features = data['employee_territories']['features']
partition_col = None

class PipelineEmployee_territories:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractEmployee_territories(row)
            result.append((df_row.get_employee_ID(), df_row.get_territory_ID()))
        df_transformed = pd.DataFrame(result, columns = employee_territories_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col