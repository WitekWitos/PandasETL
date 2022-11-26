from pandasetl.entities.orders import ExtractOrders
import pandas as pd
import json

features_copy = open(r'C:\Users\1\VSC\PandasETL\config\features.json','r', encoding='utf-8')
data = json.load(features_copy)
orders_features = data['orders']['features']
partition_col = data['orders']['partition_col']


class PipelineOrders:
    
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractOrders(row)
            result.append((df_row.get_order_id(), df_row.get_customer_id(), df_row.get_employee_id(), df_row.get_order_date(),
                          df_row.get_required_date(), df_row.get_shipped_date(), df_row.get_ship_Via(), df_row.get_freight(),
                          df_row.get_ship_name(), df_row.get_ship_address(), df_row.get_ship_city(), df_row.get_ship_region(),
                          df_row.get_ship_postal_code(), df_row.get_ship_country()))
        df_transformed = pd.DataFrame(result, columns = orders_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col
