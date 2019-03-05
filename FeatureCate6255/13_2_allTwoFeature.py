import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np


def myfind(x, y):
    idx = []
    for row in range(len(y)):
        if y[row] == x:
            idx.append(row)
    return idx


cate = 6255
userFile = "withBrandGiveTagOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userFile, 'r'))

# 初始化最大值列表和最小值列表
i = 0
feature = []
y = []
trueNum = 0
fraudNum = 0
label = []
for row in userInfo:
    if i == 0:
        i = i + 1
        label = [row[1], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                 row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
                 row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34]]
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

        if float(row[24]) > 1500000:
            row[24] = 1500000

        if float(row[27]) > 1500000:
            row[27] = 1500000

        tag = [row[1], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
               row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
               row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34]]
        feature.append(tag)
        y.append(row[35])

temparray = np.array(feature, dtype=float)
m, n = temparray.shape
# 归一化每一个特征

for i in range(n):
    for j in range(i + 1, n):
        firstFea = temparray[:, i]
        secondFea = temparray[:, j]
        fig = plt.figure(figsize=(9.6, 5.4))
        ax = fig.add_subplot(111)
        ax.set_title("Cate " + str(cate) + " Feature Scatter Plot")
        plt.xlabel(label[i])
        plt.ylabel(label[j])
        trueIdx = myfind(1, y)
        ax.scatter(firstFea[trueIdx], secondFea[trueIdx], c='r', marker='o')
        falseIdx = myfind(-1, y)
        ax.scatter(firstFea[falseIdx], secondFea[falseIdx], c='g', marker='*')
        plt.savefig("../FeatureCate" + str(cate) + "/twoFeatureScatter/Feature" + str(i) + "and" +
                    str(j) + "_Scatter.png")




