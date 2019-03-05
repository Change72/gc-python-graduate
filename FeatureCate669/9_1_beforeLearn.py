import csv
import math

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
for row in userInfo:
    if i == 0:
        i = i + 1
        continue
    else:
        if row[37] == "T":
            row[37] = 1
        else:
            row[37] = -1

        if i == 1:
            i = i + 1
            for k in range(0, featureLength):
                if k not in unusedFeatureList:
                    # init
                    maxLimitList[k] = float(row[k])
                    minLimitList[k] = float(row[k])
        else:
            for k in range(0, featureLength):
                if k not in unusedFeatureList:
                    if 0 <= float(row[k]) < minLimitList[k]:
                        minLimitList[k] = float(row[k])

                    if float(row[k]) > maxLimitList[k]:
                        maxLimitList[k] = float(row[k])

# 均分归一化
columnNum = 100
eachGap = 0.01
for k in range(0, featureLength):
    if k not in unusedFeatureList:
        if maxLimitList[k] - minLimitList[k] >= columnNum:
            eachGap = round(maxLimitList[k] - minLimitList[k] / columnNum)
        else:
            columnNum = maxLimitList[k] - minLimitList[k]

# 针对时间特征的调节
featureWithTimeList = [13, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
for k in range(0, featureLength):
    if k not in unusedFeatureList:
        if k in featureWithTimeList:
            if maxLimitList[k] > 12 * 3600:
                maxLimitList[k] = 12 * 3600

# if 0 = 0
# else = 0.5
#     if > 12*3600
#     ==1
# !0 ~ 12 * 3600 在0.5-1 junfen

userInfo = csv.reader(open(userFile, 'r'))
for row in userInfo:
    for k in range(0, featureLength):
        if k not in unusedFeatureList:
            print()
            # if columnNum < 100:
            #     # zhijie sigernor
            # else:
            #     # column -> sigernor


        tag = [row[1], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
               row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
               row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[37]]

