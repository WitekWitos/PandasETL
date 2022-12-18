from pandasetl.entities.shippers import ExtractShippers
from pandasetl.config import Config
import pandas as pd


shippers_features = Config.get_shippers_features()
partition_col = Config.get_shippers_partition_col()

class PipelineShippers:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractShippers(row)
            result.append((df_row.get_shipper_id(), df_row.get_company_name(), df_row.get_phone()))
        df_transformed = pd.DataFrame(result, columns = shippers_features)
        print(df_transformed.head(3))
        return df_transformed