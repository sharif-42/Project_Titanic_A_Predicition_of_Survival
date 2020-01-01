import pandas as pd

data = [
   {
    'name': 'Sharif',
    'age': 23,
    'blood_group': 'B+',
    'gender':'male',
     },
    {
        'name': 'Arif',
        'age': 32,
        'blood_group': 'B-'
    },
    {
        'name': 'Imran',
        'age': 25,
        'blood_group': 'AB-'
    }
]
df = pd.DataFrame(data)
df['HasBike'] = False
df.head()
print(df)

df.drop('HasBike', inplace=True, axis=1)
print(df.head())
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# data = pd.read_csv('datasets/person.csv')
# data_head = data.head(4)
# data_tail = data.tail(4)
# print(data_head)
# print('############################# tail data #######################')
# print(data_tail)
