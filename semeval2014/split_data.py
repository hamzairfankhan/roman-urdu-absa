import pandas as pd
from sklearn.model_selection import train_test_split

# Load train data
df = pd.read_csv("semeval_laptops_train.csv")

# Drop conflict labels - too ambiguous
df = df[df['label'] != 'conflict']
print(f"Total rows after dropping conflict: {len(df)}")

# Split by unique sentences to avoid data leakage
# (same sentence shouldn't appear in both train and test)
unique_sentences = df['text'].unique()
print(f"Unique sentences: {len(unique_sentences)}")

# 70% train, 15% val, 15% test
train_sents, temp_sents = train_test_split(unique_sentences, test_size=0.3, random_state=42)
val_sents, test_sents = train_test_split(temp_sents, test_size=0.5, random_state=42)

train_df = df[df['text'].isin(train_sents)]
val_df   = df[df['text'].isin(val_sents)]
test_df  = df[df['text'].isin(test_sents)]

print(f"\nTrain rows: {len(train_df)} | Unique sentences: {len(train_sents)}")
print(f"Val rows:   {len(val_df)}   | Unique sentences: {len(val_sents)}")
print(f"Test rows:  {len(test_df)}  | Unique sentences: {len(test_sents)}")

print(f"\nTrain label distribution:")
print(train_df['label'].value_counts())

# Save
train_df.to_csv("train.csv", index=False)
val_df.to_csv("val.csv", index=False)
test_df.to_csv("test.csv", index=False)

print("\nSaved train.csv, val.csv, test.csv")
