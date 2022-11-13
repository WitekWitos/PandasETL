from pandasetl.entities.regions import ExtractRegions
import pandas as pd
from config.features import region_features

class PipelineRegions:
     
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractRegions(row)
            result.append((df_row.get_region_id(), df_row.get_region_description()))
        df_transformed = pd.DataFrame(result, columns = region_features)
        print(df_transformed.head(3))
        return df_transformed