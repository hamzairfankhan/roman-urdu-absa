import pandas as pd

test = pd.read_csv("semeval_laptops_test.csv")

print("Columns:", test.columns.tolist())
print("Shape:", test.shape)
print("\nFirst 5 rows:")
print(test.head())
print("\nNull counts:")
print(test.isnull().sum())
print("\nUnique labels:")
print(test['label'].unique())
