from pandasetl.entities.territories import ExtractTerritories
import pandas as pd
import json

features_copy = open(r'C:\Users\1\VSC\PandasETL\config\features.json','r', encoding='utf-8')
data = json.load(features_copy)
territories_features = data['territories']['features']
partition_col = data['territories']['partition_col']


class PipelineTerritories:
    
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractTerritories(row)
            result.append((df_row.get_territoryID(), df_row.get_territory_description(), df_row.get_region_id()))
        df_transformed = pd.DataFrame(result, columns = territories_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col
