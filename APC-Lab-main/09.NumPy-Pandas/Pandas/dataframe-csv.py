import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "students.csv")

df = pd.read_csv(file_path)

print("DATA FROM CSV FILE:")
print(df)

print("\nFIRST FIVE RECORDS:")
print(df.head())

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nSTATISTICAL INFORMATION:")
print(df.describe())