from pandasetl.entities.customer import ExtractCustomer
from pandasetl.config import Config
import pandas as pd


customer_features = Config.get_customer_features()
partition_col = Config.get_customer_partition_col()

class PipelineCustomer:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractCustomer(row)
            result.append((df_row.get_customer_id(), df_row.get_company_name(), df_row.get_contact_name(),
                           df_row.get_contact_title(), df_row.get_address(), df_row.get_city(),
                           df_row.get_region(), df_row.get_postal_code(), df_row.get_coutry(), 
                           df_row.get_phone(), df_row.get_fax()))
        df_transformed = pd.DataFrame(result, columns = customer_features)
        print(df_transformed.head(3))
        return df_transformed