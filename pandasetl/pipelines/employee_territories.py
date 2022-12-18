from pandasetl.entities.employee_territories import ExtractEmployee_territories
from pandasetl.config import Config
import pandas as pd


employee_territories_features = Config.get_employee_territories_features()
partition_col = Config.get_employee_territories_partition_col()

class PipelineEmployee_territories:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractEmployee_territories(row)
            result.append((df_row.get_employee_ID(), df_row.get_territory_ID()))
        df_transformed = pd.DataFrame(result, columns = employee_territories_features)
        print(df_transformed.head(3))
        return df_transformed