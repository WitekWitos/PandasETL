from pandasetl.entities.order_details import ExtractOrder_details
from pandasetl.config import Config
import pandas as pd


order_details_features = Config.get_order_details_features()
partition_col = Config.get_order_details_partition_col()


class PipelineOrder_details:
    
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractOrder_details(row)
            result.append((df_row.get_order_id(), df_row.get_product_id(), df_row.get_unit_price(), 
                           df_row.get_quantity(), df_row.get_discount()))
        df_transformed = pd.DataFrame(result, columns = order_details_features)
        print(df_transformed.head(3))
        return df_transformed
