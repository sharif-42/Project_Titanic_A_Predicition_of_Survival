import pandas as pd

data = pd.read_csv('datasets/person.csv')
data_head = data.head(4)
data_tail = data.tail(4)
print(data_head)
print('############################# tail data #######################')
print(data_tail)
selected_column = ['id', 'name', 'age', 'experience','designation']
new_df = data[selected_column]
data_head =new_df.head()
#print(data_head)
#print(new_df.dtypes)
print("Working")
new_columns = {
    'id':'ID',
    'name':'NAME',
    'age':'AGE',
    'experience':'EXPERIANCE',
    'designation':'DESIGNATION',
}
new_df = new_df.rename(columns = new_columns)
print(new_df.columns)

print(new_df.describe())
print(new_df.head(4).isnull())