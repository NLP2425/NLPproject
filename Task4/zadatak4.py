import numpy as np
import pandas as pd
import statsmodels.stats.inter_rater as irr

import os

file_path = os.path.join(os.path.dirname(__file__), "Task4.csv")

df = pd.read_csv(file_path)

df_numeric = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

df_numeric = df_numeric.fillna(-1)

ratings_raw = df_numeric.to_numpy()

print("Podaci nakon čišćenja:\n", ratings_raw)

ratings, _ = irr.aggregate_raters(ratings_raw)

kappa = irr.fleiss_kappa(ratings, method='fleiss')

print("Aggregated Ratings Matrix:\n", ratings)
print(f"Fleiss' Kappa: {kappa:.4f}")
