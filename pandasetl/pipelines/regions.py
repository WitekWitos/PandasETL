from pandasetl.entities.regions import ExtractRegions
from pandasetl.config import Config
import pandas as pd


region_features = Config.get_region_features()
partition_col = Config.get_region_partition_col()

class PipelineRegions:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractRegions(row)
            result.append((df_row.get_region_id(), df_row.get_region_description()))
        df_transformed = pd.DataFrame(result, columns = region_features)
        print(df_transformed.head(3))
        return df_transformed, partition_col