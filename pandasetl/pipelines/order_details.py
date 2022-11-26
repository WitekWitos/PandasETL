from pandasetl.entities.order_details import ExtractOrder_details
import pandas as pd
import json

features_copy = open(r'C:\Users\1\VSC\PandasETL\config\features.json','r', encoding='utf-8')
data = json.load(features_copy)
order_details_features = data['order_details']['features']
partition_col = data['order_details']['partition_col']


class PipelineOrder_details:
    
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractOrder_details(row)
            result.append((df_row.get_order_id(), df_row.get_product_id(), df_row.get_unit_price(), 
                           df_row.get_quantity(), df_row.get_discount()))
        df_transformed = pd.DataFrame(result, columns = order_details_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col
