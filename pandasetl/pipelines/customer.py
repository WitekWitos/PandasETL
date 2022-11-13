from pandasetl.entities.customer import ExtractCustomer
import pandas as pd
from config.features import customer_features

class PipelineCustomer:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractCustomer(row)
            result.append((df_row.get_region(), df_row.get_postal_code(), df_row.get_coutry(), 
                           df_row.get_phone(), df_row.get_fax()))
        df_transformed = pd.DataFrame(result, columns = customer_features)
        print(df_transformed.head(3))
        return df_transformed