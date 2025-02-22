import pandas as pd
data_source = "https://www.w3schools.com/python/pandas/data.csv.txt" #add data source
df = pd.read_csv(data_source, sep = ',') #imports the data from web and assigns it to df

# Group by duration
#calculate the mean of the calories burned for each duration
grouped = df.groupby("Duration")["Calories"].mean()
print(grouped)