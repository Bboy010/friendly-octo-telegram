import pandas as pd
data_source = "https://www.w3schools.com/python/pandas/data.csv.txt" #add data source
df = pd.read_csv(data_source, sep = ',') #imports the data from web and assigns it to df


df.plot(x="Duration", y="Calories", kind="line")
plot = df["Calories"].plot(kind="hist")

print(plot)