from pandasetl.entities.suppliers import ExtractSuppliers
from pandasetl.config import Config
import pandas as pd


suppliers_features = Config.get_suppliers_features()
partition_col = Config.get_suppliers_partition_col()


class PipelineSuppliers:
    
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractSuppliers(row)
            result.append((df_row.get_supplier_id(), df_row.get_company_name(), df_row.get_contact_name(), 
                          df_row.get_contact_title(), df_row.get_address(), df_row.get_city(), df_row.get_region(),
                          df_row.get_postal_code(), df_row.get_country(), df_row.get_phone(), df_row.get_fax(), df_row.get_home_page()))
        df_transformed = pd.DataFrame(result, columns = suppliers_features)
        print(df_transformed.head(3))
        return df_transformed
