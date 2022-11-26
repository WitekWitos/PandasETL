from pandasetl.entities.regions import ExtractRegions
import pandas as pd
import json

features_copy = open(r'C:\Users\1\VSC\PandasETL\config\features.json','r', encoding='utf-8')
data = json.load(features_copy)
region_features = data['region']['features']
partition_col = data['region']['partition_col']

class PipelineRegions:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractRegions(row)
            result.append((df_row.get_region_id(), df_row.get_region_description()))
        df_transformed = pd.DataFrame(result, columns = region_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col