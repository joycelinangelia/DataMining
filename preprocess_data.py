import pandas as pd

file_path = 'contact-lenses.xlsx'
df = pd.read_excel(file_path)

# Convert categorical features to numerical (One-Hot Encoding)
df_encoded = pd.get_dummies(df, drop_first=True)

print("Encoded Data:\n", df_encoded.head())
