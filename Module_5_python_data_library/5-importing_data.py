import pandas as pd
data_source = "https://www.w3schools.com/python/pandas/data.csv.txt" #add data source
df = pd.read_csv(data_source, sep = ',') #imports the data from web and assigns it to df

print(df) #prints the data
print("="*50)
print(df.head(5)) #prints the first 5 rows
print("="*50)
print(f"Print the last 5 data : \n {df.tail(5)}") #prints the last 5 rows