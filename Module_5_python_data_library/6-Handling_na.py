import pandas as pd
data_source = "https://www.w3schools.com/python/pandas/data.csv.txt" #add data source
df = pd.read_csv(data_source, sep = ',') #imports the data from web and assigns it to df

# Drop rows with missing values
df_clean = df.dropna()
print(df_clean)
print("="*50)

# Fill missing values with a specific value
df_filled = df.fillna(0)
print(df_filled)

