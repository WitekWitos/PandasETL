from pandasetl.entities.categories import ExtractCategories
import pandas as pd
from config.features import category_features


class PipelineCategories:
    
    def executepipeline(self,df_raw,result):
    
        for row in df_raw.itertuples():
            df_row = ExtractCategories(row)
            result.append((df_row.get_category_name(), df_row.get_category_id(), 
                                df_row.get_description(), df_row.get_picture()))
        df_transformed = pd.DataFrame(result, columns = category_features)
        print(df_transformed.head(3))
        return df_transformed, # partition_col wybieramy z configa 
