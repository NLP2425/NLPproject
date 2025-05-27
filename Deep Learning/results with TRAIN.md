## LSTM

- Precision: 0.8627
- Recall: 0.3557
- F1: 0.2897
- Accuracy: 0.5924
- Confusion matrix: [[3, 213, 0], [0, 431, 0], [0, 89, 5]]

Full classification report:
              precision    recall  f1-score   support

    positive     1.0000    0.0139    0.0274       216
     neutral     0.5880    1.0000    0.7405       431
    negative     1.0000    0.0532    0.1010        94

    accuracy                         0.5924       741
   macro avg     0.8627    0.3557    0.2897       741
weighted avg     0.7604    0.5924    0.4515       741


## GRU

- Precision: 0.8623
- Recall: 0.8200
- F1: 0.8387
- Accuracy: 0.8758
- Confusion matrix: [[179, 32, 5], [17, 405, 9], [7, 22, 65]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.8818    0.8287    0.8544       216
     neutral     0.8824    0.9397    0.9101       431
    negative     0.8228    0.6915    0.7514        94

    accuracy                         0.8758       741
   macro avg     0.8623    0.8200    0.8387       741
weighted avg     0.8746    0.8758    0.8737       741


## CNN

- Precision: 0.9147
- Recall: 0.8296
- F1: 0.8632
- Accuracy: 0.8961
- Confusion matrix: [[180, 35, 1], [9, 420, 2], [10, 20, 64]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.9045    0.8333    0.8675       216
     neutral     0.8842    0.9745    0.9272       431
    negative     0.9552    0.6809    0.7950        94

    accuracy                         0.8961       741
   macro avg     0.9147    0.8296    0.8632       741
weighted avg     0.8991    0.8961    0.8930       741


