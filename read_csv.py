import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv(r"C:\Users\Sagar\Documents\rawdata\rawdata\data.csv", header=0, sep=",")

# Step 2: Filter rows where Department is "IT"
filtered_df = df[df["Department"] == "IT"]

# Step 3: Display filtered data
print(filtered_df)

# Step 4 (Optional): Save to a new CSV file
filtered_df.to_csv("filtered_data.csv", index=False)
