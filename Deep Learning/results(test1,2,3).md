## LSTM

### test1
- Precision: 0.2195
- Recall: 0.3333
- F1: 0.2647
- Accuracy: 0.6585
- Confusion matrix: [[0, 165, 0], [0, 430, 0], [0, 58, 0]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.0000    0.0000    0.0000       165
     neutral     0.6585    1.0000    0.7941       430
    negative     0.0000    0.0000    0.0000        58

    accuracy                         0.6585       653
   macro avg     0.2195    0.3333    0.2647       653
weighted avg     0.4336    0.6585    0.5229       653


### test2
- Precision: 0.1939
- Recall: 0.3333
- F1: 0.2452
- Accuracy: 0.5816
- Confusion matrix: [[0, 216, 0], [0, 431, 0], [0, 94, 0]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.0000    0.0000    0.0000       216
     neutral     0.5816    1.0000    0.7355       431
    negative     0.0000    0.0000    0.0000        94

    accuracy                         0.5816       741
   macro avg     0.1939    0.3333    0.2452       741
weighted avg     0.3383    0.5816    0.4278       741


### test3
- Precision: 0.1106
- Recall: 0.3333
- F1: 0.1660
- Accuracy: 0.3317
- Confusion matrix: [[0, 267, 0], [0, 263, 0], [0, 263, 0]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.0000    0.0000    0.0000       267
     neutral     0.3317    1.0000    0.4981       263
    negative     0.0000    0.0000    0.0000       263

    accuracy                         0.3317       793
   macro avg     0.1106    0.3333    0.1660       793
weighted avg     0.1100    0.3317    0.1652       793


## GRU

### test1
- Precision: 0.4470
- Recall: 0.4538
- F1: 0.4485
- Accuracy: 0.6064
- Confusion matrix: [[86, 69, 10], [97, 302, 31], [16, 34, 8]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.4322    0.5212    0.4725       165
     neutral     0.7457    0.7023    0.7234       430
    negative     0.1633    0.1379    0.1495        58

    accuracy                         0.6064       653
   macro avg     0.4470    0.4538    0.4485       653
weighted avg     0.6147    0.6064    0.6090       653


### test2
- Precision: 0.8557
- Recall: 0.8500
- F1: 0.8527
- Accuracy: 0.8880
- Confusion matrix: [[191, 19, 6], [20, 397, 14], [9, 15, 70]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.8682    0.8843    0.8761       216
     neutral     0.9211    0.9211    0.9211       431
    negative     0.7778    0.7447    0.7609        94

    accuracy                         0.8880       741
   macro avg     0.8557    0.8500    0.8527       741
weighted avg     0.8875    0.8880    0.8877       741


### test3
- Precision: 0.6896
- Recall: 0.6454
- F1: 0.6251
- Accuracy: 0.6456
- Confusion matrix: [[187, 58, 22], [21, 237, 5], [41, 134, 88]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.7510    0.7004    0.7248       267
     neutral     0.5524    0.9011    0.6850       263
    negative     0.7652    0.3346    0.4656       263

    accuracy                         0.6456       793
   macro avg     0.6896    0.6454    0.6251       793
weighted avg     0.6899    0.6456    0.6256       793


## CNN

### test1
- Precision: 0.6103
- Recall: 0.4595
- F1: 0.4816
- Accuracy: 0.6692
- Confusion matrix: [[61, 103, 1], [59, 367, 4], [11, 38, 9]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.4656    0.3697    0.4122       165
     neutral     0.7224    0.8535    0.7825       430
    negative     0.6429    0.1552    0.2500        58

    accuracy                         0.6692       653
   macro avg     0.6103    0.4595    0.4816       653
weighted avg     0.6505    0.6692    0.6416       653


### test2
- Precision: 0.9077
- Recall: 0.8366
- F1: 0.8659
- Accuracy: 0.8988
- Confusion matrix: [[180, 33, 3], [9, 420, 2], [11, 17, 66]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.9000    0.8333    0.8654       216
     neutral     0.8936    0.9745    0.9323       431
    negative     0.9296    0.7021    0.8000        94

    accuracy                         0.8988       741
   macro avg     0.9077    0.8366    0.8659       741
weighted avg     0.9000    0.8988    0.8960       741


### test3
- Precision: 0.7336
- Recall: 0.5839
- F1: 0.5465
- Accuracy: 0.5839
- Confusion matrix: [[152, 109, 6], [5, 258, 0], [25, 185, 53]]

Full classification report:
              precision    recall  f1-score   support

    positive     0.8352    0.5693    0.6771       267
     neutral     0.4674    0.9810    0.6331       263
    negative     0.8983    0.2015    0.3292       263

    accuracy                         0.5839       793
   macro avg     0.7336    0.5839    0.5465       793
weighted avg     0.7341    0.5839    0.5471       793


