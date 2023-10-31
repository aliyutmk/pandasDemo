import pandas as pd

df = pd.read_csv("data/car-sharing-record.csv") #, sep='\t'

# view the first 2 rows
print(df.head(2))

#return the names of the columns in the dataset
print(df.columns)
#access the row potion of the data
print(df.index)
#access the body of the data
print(df.values)

print(type(df))

#the number of rows and columns
print(df.shape)

print(df.size)

print(df.info())

#print the information of a particular column
print(df['realobjektname'])

#get a subset of my data
subset = df[['buchungsanfang', 'buchungsende', 'buchungssequenznummer', 'realobjektname', 'realobjektnummer', 'buchungszieltyp', 'kilometer']]
print(subset)