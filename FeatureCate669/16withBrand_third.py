import csv
import math
import numpy as np
import random
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.decomposition import PCA

cate = 669
userFile = "withBrandGiveTagOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userFile, 'r'))

featureLength = 35
unusedFeatureList = [0, 2, 3]
timestampFeatureList = [13, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]     # 11
numFeatureList = [4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]     # 20

i = 0
feature = []
y = []
trueNum = 0
fraudNum = 0
for row in userInfo:
    if i == 0:
        i = i + 1
        continue
    else:
        if row[35] == "True":
            row[35] = 1
            trueNum = trueNum + 1
        elif row[35] == "False":
            row[35] = -1
            fraudNum = fraudNum + 1
        else:
            continue

        tag = [row[1], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
               row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
               row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34]]
        tag = [abs(float(i)) for i in tag]
        feature.append(tag)
        y.append(row[35])

user_FeatureRecord = ['user', 'brand', 'user_Truthful', 'user_FraudBuyNum',
                      'user_BrandPv', 'user_BrandFav', 'user_BrandCart', 'user_BrandBuy',
                      'user_CatePv', 'user_CateFav', 'user_CateCart', 'user_CateBuy',
                      'user_ReBuyNum', 'user_ReBuyTimeGap',
                      'user_TimesFromPvToBuy', 'user_TimesFromFavToBuy', 'user_TimesFromCartToBuy',
                      'user_OtherNumFromPvToBuy', 'user_OtherNumFromFavToBuy', 'user_OtherNumFromCartToBuy',
                      'user_OtherNumFromBuyToBuy', 'user_OtherTimesFromPvToBuy', 'user_OtherTimesFromFavToBuy',
                      'user_OtherTimesFromCartToBuy', 'user_OtherTimesFromBuyToBuy',
                      'user_BrandPvToBuyTime', 'user_BrandFavToBuyTime', 'user_BrandCartToBuyTime',
                      'user_CatePvToBuyTime', 'user_CateFavToBuyTime', 'user_CateCartToBuyTime',
                      'user_BrandViewTime', 'user_CateViewTime', 'user_ReBuyBrandViewTime', 'user_ReBuyCateViewTime']

temparray = np.array(feature, dtype=float)
m, n = temparray.shape
# 归一化每一个特征
for j in range(n):
    features = temparray[:, j]
    meanVal = np.mean(features, axis=0)
    std = np.std(features, axis=0)
    if std != 0:
        # temparray[:, j] = (features - meanVal) / std
        temparray[:, j] = features / std
    else:
        temparray[:, j] = 0

maxFeature = 23
timestampMaxFeature = 6
numMaxFeature = 12
model2 = SelectKBest(chi2, k=maxFeature)#选择k个最佳特征
model2.fit_transform(temparray, y)
# model2.fit_transform(final, y)
featureScore = model2.scores_.tolist()
maxIndex = [0]
timestampNumTag = 0
numTag = 0
for i in range(maxFeature):
    index = featureScore.index(max(featureScore))
    if index in timestampFeatureList and timestampNumTag < timestampMaxFeature:
        maxIndex.append(index)
        timestampNumTag = timestampNumTag + 1

    if index in numFeatureList and numTag < numMaxFeature:
        maxIndex.append(index)
        numTag = numTag + 1

    featureScore[index] = 0

print(maxIndex)


# k = 0
# for i in range(featureLength):
#     while k in unusedFeatureList:
#         k = k + 1
#     if k < featureLength:
#         print(k, i, user_FeatureRecord[k], model2.scores_[i])
#         k = k + 1

finalFeature = []
# for row in final:
for row in temparray:
    # temp = [row[11], row[12], row[13], row[16], row[18], row[20], row[22], row[25],
    #         row[27], row[28], row[29]]
    temp = []
    for i in maxIndex:
        temp.append(row[i])
    finalFeature.append(temp)

temparray = np.array(finalFeature, dtype=float)

trainRate = 0.8
x_trainSeq = random.sample(list(range(0, trueNum)), int(math.floor(trainRate * trueNum)))
y_trainSeq = random.sample(list(range(0, fraudNum)), int(math.floor(trainRate * fraudNum)))

x_train = []
x_test = []
y_train = []
y_test = []

trueRecord = 0
fraudRecord = 0
for i in list(range(0, m)):
    if y[i] == 1:
        if trueRecord in x_trainSeq:
            x_train.append(temparray[i])
            y_train.append(y[i])
        else:
            x_test.append(temparray[i])
            y_test.append(y[i])
        trueRecord = trueRecord + 1
    else:
        if fraudRecord in y_trainSeq:
            x_train.append(temparray[i])
            y_train.append(y[i])
        else:
            x_test.append(temparray[i])
            y_test.append(y[i])
        fraudRecord = fraudRecord + 1

classifier = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr', probability=True)
# classifier = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
classifier.fit(x_train, y_train)

print("训练集准确率" + str(classifier.score(x_train, y_train)))  # 精度
y_hat = classifier.predict(x_train)
print(y_hat)
# num = 0
# for i in list(range(0, len(y_train))):
#     if y_train[i] == y_hat[i]:
#         num = num + 1
#
# print(num / len(y_train))
print("测试集准确率" + str(classifier.score(x_test, y_test)))
y_hat = classifier.predict(x_test)
print(y_hat)
fraudTestNum = 0
recognizeNum = 0
trueTestNum = 0
falseRecognizeNum = 0
for i in range(len(y_hat)):
    print(y_test[i], y_hat[i])
    if y_test[i] == -1:
        fraudTestNum = fraudTestNum + 1
        if y_hat[i] == -1:
            recognizeNum = recognizeNum + 1
    if y_test[i] == 1:
        trueTestNum = trueTestNum + 1
        if y_hat[i] == -1:
            falseRecognizeNum = falseRecognizeNum + 1

print(recognizeNum / fraudTestNum)
print(falseRecognizeNum / trueTestNum)
# print(y_test)

#效果评估：
#准确率：scikit-learn提供了accuracy_score来计算：LogisticRegression.score()
#准确率是分类器预测正确性的比例，但是并不能分辨出假阳性错误和假阴性错误
# cv 交叉验证 次数
print("交叉验证：")
scores = cross_val_score(classifier, x_train, y_train, cv=5)
print('训练准确率：', np.mean(scores), scores)

scores = cross_val_score(classifier, x_test, y_test, cv=5)
print('测试准确率：', np.mean(scores), scores)

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
plt.title('SVM Receiver Operating Characteristic')
plt.plot(false_positive_rate, recall, 'b', label='AUC = %0.2f' % roc_auc)
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.ylabel('Recall')
plt.xlabel('Fall-out')
plt.show()
# plt.savefig("../FeatureCate" + str(cate) + "/SVM_ROC.png")


