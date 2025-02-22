import pandas as pd
data_source = "https://www.w3schools.com/python/pandas/data.csv.txt" #add data source
df = pd.read_csv(data_source, sep = ',') #imports the data from web and assigns it to df

duration = df.loc[df['Duration'] == 60]
print(duration)