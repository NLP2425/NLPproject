## LSTM

- Precision: 0.3611
- Recall: 0.3422
- F1: 0.2860
- Accuracy: 0.5735
- Confusion matrix: [[14, 200, 2], [16, 410, 5], [8, 85, 1]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.3684    0.0648    0.1102       216
     neutral     0.5899    0.9513    0.7282       431
    negative     0.1250    0.0106    0.0196        94

    accuracy                         0.5735       741
   macro avg     0.3611    0.3422    0.2860       741
weighted avg     0.4664    0.5735    0.4582       741


## GRU

- Precision: 0.4206
- Recall: 0.3942
- F1: 0.3966
- Accuracy: 0.4953
- Confusion matrix: [[93, 112, 11], [150, 260, 21], [33, 47, 14]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.3370    0.4306    0.3780       216
     neutral     0.6205    0.6032    0.6118       431
    negative     0.3043    0.1489    0.2000        94

    accuracy                         0.4953       741
   macro avg     0.4206    0.3942    0.3966       741
weighted avg     0.4978    0.4953    0.4914       741


## CNN

- Precision: 0.5362
- Recall: 0.3834
- F1: 0.3606
- Accuracy: 0.5965
- Confusion matrix: [[36, 178, 2], [27, 401, 3], [9, 80, 5]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.5000    0.1667    0.2500       216
     neutral     0.6085    0.9304    0.7358       431
    negative     0.5000    0.0532    0.0962        94

    accuracy                         0.5965       741
   macro avg     0.5362    0.3834    0.3606       741
weighted avg     0.5631    0.5965    0.5130       741


