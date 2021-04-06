import pandas as pd

def to_csv(tranformed_data:dict, output_file:str)->pd.DataFrame:
    return pd.DataFrame(tranformed_data).to_csv(output_file)
