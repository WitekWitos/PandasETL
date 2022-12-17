from pandasetl.entities.products import ExtractProducts
from pandasetl.config import Config
import pandas as pd


products_features = Config.get_products_features()
partition_col = Config.get_products_partition_col()

class PipelineProducts:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractProducts(row)
            result.append((df_row.get_product_id(), df_row.get_product_name(), df_row.get_supplier_id(), df_row.get_category_id(),
                          df_row.get_quantityPerUnit(), df_row.get_unit_price(), df_row.get_units_in_stock(),
                          df_row.get_units_on_order(), df_row.get_reorder_level(), df_row.get_discontinued()))
        df_transformed = pd.DataFrame(result, columns = products_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col