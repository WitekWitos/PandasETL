from pandasetl.entities.shippers import ExtractShippers
import pandas as pd
from config.features import shippers_features

class PipelineShippers:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractShippers(row)
            result.append((df_row.get_shipper_id(), df_row.get_company_name(), df_row.get_phone()))
        df_transformed = pd.DataFrame(result, columns = shippers_features)
        print(df_transformed.head(3))
        return df_transformed