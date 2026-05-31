import pandas as pd

print("File is running")

df = pd.read_csv("creditcard.csv")

print(df.head())
print(df.shape)