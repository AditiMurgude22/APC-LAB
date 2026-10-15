# PROGRAM 5: CREATE AND DISPLAY A PANDAS DATAFRAME

import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Sahil", "Neha"],
    "Age": [20, 21, 20, 22],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("PANDAS DATAFRAME:")
print(df)

print("\nFIRST TWO ROWS:")
print(df.head(2))

print("\nSTUDENT NAMES:")
print(df["Name"])

print("\nSTUDENT MARKS:")
print(df["Marks"])