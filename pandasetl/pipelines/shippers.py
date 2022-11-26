from pandasetl.entities.shippers import ExtractShippers
import pandas as pd
import json

features_copy = open(r'C:\Users\1\VSC\PandasETL\config\features.json','r', encoding='utf-8')
data = json.load(features_copy)
shippers_features = data['shippers']['features']
partition_col = data['shippers']['partition_col']

class PipelineShippers:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractShippers(row)
            result.append((df_row.get_shipper_id(), df_row.get_company_name(), df_row.get_phone()))
        df_transformed = pd.DataFrame(result, columns = shippers_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col