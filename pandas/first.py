import pandas as pd

data = {

    'Name': ['Aarav Sharma', 'Rohan Patel'],
    'Age': [20, 24]

}

df = pd.DataFrame(data)
print(df)
df = pd.read_csv('pandas.csv')
df.head()
df.tail()
df.info()
df.describe()
df['name']
df['age']
df[df['age'] > 22]
df.loc[3, 'name']

df['age_plus_10'] = df['age'] + 10

df.drop('age_plus_10', axis=1, inplace=True)

