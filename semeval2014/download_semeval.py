from datasets import load_dataset

# Load SemEval 2014 Laptops dataset
dataset = load_dataset("tomaarsen/setfit-absa-semeval-laptops")

# Check what it looks like
print(dataset)
print(dataset["train"][0])

# Save to CSV for easy viewing
dataset["train"].to_csv("semeval_laptops_train.csv", index=False)
dataset["test"].to_csv("semeval_laptops_test.csv", index=False)

print("Done! Files saved.")
