import pandas as pd
from scipy.spatial.distance import cosine
def train_data():
    path='app/data_to_csv.csv'
    data = pd.read_csv(path)
    # --- Start Item Based Recommendations --- #
    # Drop any column named "user"
    data_item_base = data.drop('_uid',1)
    data_item_base_frame = pd.DataFrame(index=data_item_base.columns, columns=data_item_base.columns)
    path_data_save='app/data_item_base_frame.csv'
    for i in range(0, len(data_item_base_frame.columns)):
        # Loop through the columns for each column
        for j in range(0, len(data_item_base_frame.columns)):
            # Calculate similarity
            print(i ,j)
            data_item_base_frame.iloc[i, j] = 1 - cosine(data.iloc[:, i], data.iloc[:, j])
    data_item_base_frame.to_csv(path_data_save, sep=',', encoding='utf-8')
        # data_item_base_frame = pd.read_csv('data_item_base_frame.csv')
    data_item_base_frame=pd.read_csv(path_data_save);
    return data_item_base_frame