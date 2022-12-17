from pandasetl.entities.orders import ExtractOrders
from pandasetl.config import Config
import pandas as pd


orders_features = Config.get_orders_features()
partition_col = Config.get_orders_partition_col()


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
