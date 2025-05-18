## Annotation Guidelines

3-label system:

| Label | Sentiment |
|-------|-----------|
| 0     | Positive  |
| 1     | Neutral   |
| 2     | Negative  |


| Metod | Algoritam | Skup | Test 1 (Prec/Rec/F1/Acc) | Test 2 (Prec/Rec/F1/Acc) | Test 3 (Prec/Rec/F1/Acc) |
|-------|-----------|------|--------------------------|--------------------------|--------------------------|
| Machine learning | Logistic regression | Train2 | 0.583 / 0.587 / 1 / 0.584 / 0.587 | 0.572 / 0.606 / 1 / 0.573 / 0.606 | 0.528 / 0.465 / 1 / 0.427 / 0.465 |
| Machine learning | Logistic regression | Test | 0.945 / 0.940 / 1 / 0.938 / 0.940 | 0.965 / 0.964 / 1 / 0.963 / 0.964 | 0.982 / 0.982 / 1 / 0.982 / 0.982 |
| Machine learning | Decision tree classifier | Train2 | 0.532 / 0.481 / 1 / 0.502 / 0.481 | 0.511 / 0.493 / 1 / 0.501 / 0.493 | 0.423 / 0.401 / 1 / 0.393 / 0.401 |
| Machine learning | Decision tree classifier | Test | 1.000 / 1.000 / 1 / 1.000 / 1.000 | 0.999 / 0.999 / 1 / 0.999 / 0.999 | 0.999 / 0.999 / 1 / 0.999 / 0.999 |


## New code 
In the initial code, we were unable to achieve satisfactory scores, so we made certain modifications. The following changes were introduced in the updated code:

* `max_iter=5000` in **Logistic Regression**
* `kernel='rbf'` in **SVM**
* `TfidfVectorizer(max_features=5000, ngram_range=(1, 3))`

Updated code: [https://github.com/NLP2425/NLPproject/blob/main/Machine%20Learning/corrected%20version.ipynb](https://github.com/NLP2425/NLPproject/blob/main/Machine%20Learning/corrected%20version.ipynb)
