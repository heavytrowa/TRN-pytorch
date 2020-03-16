import csv

TP = 0
TN = 0
FP = 0
FN = 0

count = 0
hit = 0

with open('result_try.csv') as result_file:
    reader = csv.reader(result_file, delimiter = ',')
    for row in reader:
        count += 1
        label = row[1]
        prediction = row[3]
        if label==prediction:
            hit += 1
        if label == "slipping" and prediction == "slipping":
            TP += 1
        elif label != "slipping" and prediction != "slipping":
            TN += 1
        elif label != "slipping" and prediction == "slipping":
            FP += 1
        elif label == "slipping" and prediction != "slipping":
            FN += 1
print(TP,TN)
print(count)
print(hit)
accuracy = float(TP+TN) / float(count)
precision = float(TP)/ float(TP+FP)
recall = float(TP)/ float(TP+FN)
acc_multi = float(hit) / float(count)

print("accuracy: " + str(accuracy))
print("precision: " + str(precision))
print("recall: " + str(recall))
print("acc_multi: " + str(acc_multi))
