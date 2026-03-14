import pandas as pd

train = pd.read_csv("semeval_laptops_train.csv")
test = pd.read_csv("semeval_laptops_test.csv")

print("=== TRAIN SET ===")
print(f"Total rows: {len(train)}")
print(f"Unique sentences: {train['text'].nunique()}")
print(f"\nLabel distribution:")
print(train['label'].value_counts())

print("\n=== TEST SET ===")
print(f"Total rows: {len(test)}")
print(f"Unique sentences: {test['text'].nunique()}")
print(f"\nLabel distribution:")
print(test['label'].value_counts())

print("\n=== SAMPLE ROWS ===")
print(train.head(10).to_string())
