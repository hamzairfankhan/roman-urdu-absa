# Roman Urdu ABSA

Zero-shot aspect-based sentiment analysis for Roman Urdu e-commerce reviews, comparing English BERT with multilingual BERT after SemEval 2014 training.

## Results

| Model | SemEval macro-F1 | Roman Urdu zero-shot macro-F1 |
|---|---:|---:|
| BERT | 0.6838 | 0.2700 |
| mBERT | 0.6410 | **0.3548** |

mBERT retained substantially more cross-lingual signal, especially for negative sentiment recall (0.702 vs. 0.112).

## Dataset snapshot

- 842 aspect-level annotations
- 389 unique reviews
- 24 normalized aspect categories
- 410 positive, 295 negative, and 137 neutral labels

## Run

```bash
pip install -r requirements.txt
```

Place `daraz_dataset.csv` in the repository root and run `notebooks/absa_roman_urdu.ipynb`. The raw review file is not redistributed until per-row provenance and redistribution terms are documented.

This is a cross-domain, cross-lingual baselineâ€”not a production sentiment system.

