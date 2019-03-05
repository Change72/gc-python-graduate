from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
import csv
import random
import math
from sklearn.model_selection import train_test_split, cross_val_score


def show_accuracy(y_hat, y_test, param):
    pass


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
        tag = [row[1], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
               row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
               row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[37]]
        # if i < 5:
        #     print(tag)
    #     i = i + 1
        feature.append(tag)

feature = np.array(feature)
x, y = np.split(feature, (32,), axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.8)

classifier = LogisticRegression()  # 使用类，参数全是默认的
classifier.fit(x_train, y_train.ravel())  # 训练数据来学习，不需要返回值
# print(np.dtype(x_test))

x_train = np.array(x_train, dtype=float)
y_train = np.array(y_train, dtype=float)
x_test = np.array(x_test, dtype=float)
y_test = np.array(y_test, dtype=float)
predictions = classifier.predict(x_test)
print(predictions)
#效果评估：
#准确率：scikit-learn提供了accuracy_score来计算：LogisticRegression.score()
#准确率是分类器预测正确性的比例，但是并不能分辨出假阳性错误和假阴性错误
scores = cross_val_score(classifier, x_train, y_train, cv=5)
print('准确率：', np.mean(scores), scores)

scores = cross_val_score(classifier, x_test, y_test, cv=5)
print('准确率：', np.mean(scores), scores)
# print(classifier.score(x_train, y_train))  # 精度
# y_hat = classifier.predict(x_train)
# show_accuracy(y_hat, y_test, '训练集')
# print(classifier.score(x_test, y_test))
# y_hat = classifier.predict(x_test)
# show_accuracy(y_hat, y_test, '测试集')
