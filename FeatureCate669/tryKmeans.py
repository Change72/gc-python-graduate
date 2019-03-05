from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn import cluster
import numpy as np
import scipy
import matplotlib.pyplot as plt
import csv

cate = 669
userInfoFile = "second_kMeansOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userInfoFile, 'r'))

userFeature = []
for row in userInfo:
    userFeature.append(row)

data = np.array(userFeature)


# 生成10*3的矩阵
# data = np.random.rand(100, 3)

# 聚类为4类
estimator = KMeans(n_clusters=3)
# fit_predict表示拟合+预测，也可以分开写
res = estimator.fit_predict(data)
# 预测类别标签结果
lable_pred = estimator.labels_
# 各个类别的聚类中心值
centroids = estimator.cluster_centers_
# 聚类中心均值向量的总和
inertia = estimator.inertia_
print(data)
print(lable_pred)

# for i in range(len(data)):
#     if int(lable_pred[i]) == 0:
#         plt.scatter(data[i][28], data[i][29], color='red')
#     if int(lable_pred[i]) == 1:
#         plt.scatter(data[i][28], data[i][29], color='black')
#     # if int(lable_pred[i]) == 2:
#     #     plt.scatter(data[i][0], data[i][1], color='blue')
# plt.show()

# user_FeatureRecord = ['user', 'brand', 'user_Truthful', 'user_FraudBuyNum',
#                       'user_BrandPv', 'user_BrandFav', 'user_BrandCart', 'user_BrandBuy',
#                       'user_CatePv', 'user_CateFav', 'user_CateCart', 'user_CateBuy',
#                       'user_ReBuyNum', 'user_ReBuyTimeGap',
#                       'user_TimesFromPvToBuy', 'user_TimesFromFavToBuy', 'user_TimesFromCartToBuy',
#                       'user_OtherNumFromPvToBuy', 'user_OtherNumFromFavToBuy', 'user_OtherNumFromCartToBuy',
#                       'user_OtherNumFromBuyToBuy', 'user_OtherTimesFromPvToBuy', 'user_OtherTimesFromFavToBuy',
#                       'user_OtherTimesFromCartToBuy', 'user_OtherTimesFromBuyToBuy',
#                       'user_BrandPvToBuyTime', 'user_BrandFavToBuyTime', 'user_BrandCartToBuyTime',
#                       'user_CatePvToBuyTime', 'user_CateFavToBuyTime', 'user_CateCartToBuyTime',
#                       'user_BrandViewTime', 'user_CateViewTime', 'user_ReBuyBrandViewTime',
#                       'user_ReBuyCateViewTime', 'user_GiveTag']
#
userFile = "second_three_tryKMeansOfCate" + str(cate) + ".csv"
#
# # 记录用户行为信息
# uf = open(userFile, 'a', newline='')
# uWriter = csv.writer(uf)
# uWriter.writerow(user_FeatureRecord)
# uf.close()
i = 0

userInfoFile = "giveTagOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userInfoFile, 'r'))

for row in userInfo:
    row.append("0")
    if row[35] == "False":
        row[36] = lable_pred[i]
        i = i + 1

    uf = open(userFile, 'a', newline='')
    uWriter = csv.writer(uf)
    uWriter.writerow(row)
    uf.close()


