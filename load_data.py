import pandas as pd

# Load the dataset
file_path = 'contact-lenses.xlsx'
df = pd.read_excel(file_path)

# View the first few rows
print(df.head())

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# View data types
print("Data types:\n", df.info())
