from pandasetl.entities.categories import ExtractCategories
import pandas as pd
import json

features_copy = open(r'C:\Users\1\VSC\PandasETL\config\features.json','r', encoding='utf-8')
data = json.load(features_copy)
category_features = data['category']['features']
partition_col = data['category']['partition_col']


class PipelineCategories:
    
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractCategories(row)
            result.append((df_row.get_category_name(), df_row.get_category_id(), 
                                df_row.get_description(), df_row.get_picture()))
        df_transformed = pd.DataFrame(result, columns = category_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col
