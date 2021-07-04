import pandas as pd

import os
from train import train_data
 
path='data_to_csv.csv'
data = pd.read_csv(path)
# --- Start Item Based Recommendations --- #
# Drop any column named "user"
data_item_base = data.drop('_uid',1)

path_data_save='data_item_base_frame.csv'
if not os.path.exists(path_data_save):
    data_item_base_frame=train_data();
data_item_base_frame=pd.read_csv(path_data_save);

data_neighbors = pd.DataFrame(index=data_item_base_frame.columns, columns = range(1, 12))
# Order by similarity
for i in range(0, len(data_item_base_frame.columns)):
    data_neighbors.iloc[i,:11] = data_item_base_frame.iloc[0:, i].sort_values(ascending=False)[:11].index
print(data_neighbors.head(10).iloc[:,0:11])