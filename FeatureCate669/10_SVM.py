from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
import csv
import random
import math
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

def sigmoid(x, usestatus):
    if usestatus:
        return (1.0 / (1 + np.exp(- float(x))) - 0.5) * 2
    else:
        return float(x)


def MaxMinNormalization(x, Max, Min):
    x = (x - Min) / (Max - Min)
    return x


cate = 669
srcFile = "second_fourth_final_tryKMeansOfCate" + str(cate) + ".csv"

featureInfo = csv.reader(open(srcFile, 'r'))
feature = []
tag = []

i = 0
for row in featureInfo:
    if i == 0:
        i = i + 1
        continue
    else:
        if row[37] == "T":
            row[37] = 1
        else:
            row[37] = -1

        # row.remove(row[36])
        # row.remove(row[35])
        # row.remove(row[3])
        # row.remove(row[2])
        # row.remove(row[0])
        tag = [row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
               row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
               row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[37]]
        if i < 5:
            print(tag)
            i = i + 1
        feature.append(tag)

feature = np.array(feature)

x, y = np.split(feature, (31,), axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.9)

k = 0
final_train = []
for i in x_train:
    tag = []
    for j in i:
        temp = sigmoid(float(j), True)
        tag.append(temp)
    final_train.append(tag)

y_train = np.array(y_train, dtype=float)

classifier = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr')
# classifier = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
classifier.fit(final_train, y_train.ravel())

print(classifier.score(final_train, y_train))  # 精度
y2_hat = classifier.predict(final_train)
print(y2_hat)

final_test = []
for i in x_test:
    tag = []
    for j in i:
        temp = sigmoid(float(j), True)
        tag.append(temp)
    final_test.append(tag)

print(final_test)

y_test = np.array(y_test, dtype=float)
print(classifier.score(final_test, y_test))
y_hat = classifier.predict(final_test)
print(y_hat)
#效果评估：
#准确率：scikit-learn提供了accuracy_score来计算：LogisticRegression.score()
#准确率是分类器预测正确性的比例，但是并不能分辨出假阳性错误和假阴性错误
# cv 交叉验证 次数
scores = cross_val_score(classifier, x_train, y_train, cv=5)
print('准确率：', np.mean(scores), scores)

scores = cross_val_score(classifier, x_test, y_test, cv=5)
print('准确率：', np.mean(scores), scores)

precisions = cross_val_score(classifier, x_train, y_train, cv=5, scoring='precision')
print(u'精确率：', np.mean(precisions), precisions)
recalls = cross_val_score(classifier, x_train, y_train, cv=5, scoring='recall')
print(u'召回率：', np.mean(recalls), recalls)
plt.scatter(recalls, precisions)

# 综合评价指标
f1s = cross_val_score(classifier, x_train, y_train, cv=5, scoring='f1')
print('综合评价指标：', np.mean(f1s), f1s)
# 综合评价指标是80%。由于精确率和召回率的差异比较小，所以综合评价指标的罚值也比较小。有时也会用F0.5和F2，表示精确率权重大于召回率，或召回率权重大于精确率。

# ROC AUC
# ROC曲线（Receiver Operating Characteristic，ROC curve）可以用来可视化分类器的效果。和准确率不同，ROC曲线对分类比例不平衡的数据集不敏感，ROC曲线显示的是对超过限定阈值的所有预测结果的分类器效果。ROC曲线画的是分类器的召回率与误警率（fall-out）的曲线。误警率也称假阳性率，是所有阴性样本中分类器识别为阳性的样本所占比例：
# F=FP/(TN+FP) AUC是ROC曲线下方的面积，它把ROC曲线变成一个值，表示分类器随机预测的效果. from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_curve, auc

predictions = classifier.predict_proba(x_test)
false_positive_rate, recall, thresholds = roc_curve(y_test, predictions[:, 1])
roc_auc = auc(false_positive_rate, recall)
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, recall, 'b', label='AUC = %0.2f' % roc_auc)
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.ylabel('Recall')
plt.xlabel('Fall-out')
plt.savefig("../FeatureCate" + str(cate) + "/LR_ROC.png")
