from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

import csv
import math
import numpy as np
import random
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

cate = 669
userFile = "second_fourth_final_tryKMeansOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userFile, 'r'))
userDirFile = "normalize_tryKMeansOfCate" + str(cate) + ".csv"

featureLength = 37
maxLimitList = list(range(0, featureLength))
minLimitList = list(range(0, featureLength))
unusedFeatureList = [0, 2, 3, 35, 36]

# 初始化最大值列表和最小值列表
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
        # if row[37] == "T":
        #     row[37] = 1
        #     trueNum = trueNum + 1
        # else:
        #     row[37] = -1
        #     fraudNum = fraudNum + 1

        tag = [row[1], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
               row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
               row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34]]
        tag = [float(i) for i in tag]
        feature.append(tag)
        y.append(row[37])

# model1 = SelectKBest(chi2, k=2)#选择k个最佳特征
# model1.fit_transform(feature, y)
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
# k = 0
# for i in range(featureLength):
#     while k in unusedFeatureList:
#         k = k + 1
#     if k < featureLength:
#         print(k, i, user_FeatureRecord[k], model1.scores_[i])
#         k = k + 1




temparray = np.array(feature, dtype=float)
m, n = temparray.shape
# 归一化每一个特征
for j in range(n):
    features = temparray[:, j]
    meanVal = np.mean(features, axis=0)
    std = np.std(features, axis=0)
    if std != 0:
        # temparray[:, j] = (features - meanVal) / std
        temparray[:, j] = (features - meanVal) / std
    else:
        temparray[:, j] = 0
    print(j)
    print(max(temparray[:, j]))
    print(min(temparray[:, j]))
    print(meanVal / std)


# model2 = SelectKBest(chi2, k=2)#选择k个最佳特征
# model2.fit_transform(temparray, y)
#
# k = 0
# for i in range(featureLength):
#     while k in unusedFeatureList:
#         k = k + 1
#     if k < featureLength:
#         print(k, i, user_FeatureRecord[k], model2.scores_[i])
#         k = k + 1



