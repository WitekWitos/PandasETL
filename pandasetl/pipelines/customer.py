from pandasetl.entities.customer import ExtractCustomer
import pandas as pd
import json

features_copy = open(r'C:\Users\1\VSC\PandasETL\config\features.json','r', encoding='utf-8')
data = json.load(features_copy)
customer_features = data['customer']['features']
partition_col = data['customer']['partition_col']


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
        return df_transformed, partition_col