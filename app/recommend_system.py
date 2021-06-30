import pandas as pd
from scipy.spatial.distance import cosine
import os
def recommnend_data(_id):
    path='app/data_to_csv.csv'
    data = pd.read_csv(path)
    # --- Start Item Based Recommendations --- #
    # Drop any column named "user"
    data_item_base = data.drop('_uid',1)
    _id_data=data_item_base.columns
    data_item_base_frame = pd.DataFrame(index=data_item_base.columns, columns=data_item_base.columns)
    path_data_save='app/data_item_base_frame.csv'
    if not os.path.exists(path_data_save):
        for i in range(0, len(data_item_base_frame.columns)):
            # Loop through the columns for each column
            for j in range(0, len(data_item_base_frame.columns)):
                # Calculate similarity
                data_item_base_frame.iloc[i, j] = 1 - cosine(data.iloc[:, i], data.iloc[:, j])
        data_item_base_frame.to_csv(path_data_save, sep=',', encoding='utf-8')
        # data_item_base_frame = pd.read_csv('data_item_base_frame.csv')
    data_item_base_frame=pd.read_csv(path_data_save);

    data_neighbors = pd.DataFrame(index=data_item_base_frame.columns, columns = range(1, 12))
    # Order by similarity
    for i in range(0, len(data_item_base_frame.columns)):
        data_neighbors.iloc[i,:11] = data_item_base_frame.iloc[0:, i].sort_values(ascending=False)[:11].index
    temp= data_neighbors.loc[_id];
    result=[];
    for i in range(2,12):
        result.append(_id_data[temp[i]])
    return result