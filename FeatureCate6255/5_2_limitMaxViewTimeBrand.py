import csv
import math
from pylab import *
from matplotlib.ticker import MultipleLocator

majorGap = 20
xMajorLocator = MultipleLocator(majorGap)  # 将x主刻度标签设置为20的倍数
xMinorLocator = MultipleLocator(5)  # 将x轴次刻度标签设置为5的倍数

cate = 6255

brandBuyLimitNum = 500
brandList = []
brandInfoFile = "brandFeatureOfCate" + str(cate) + ".csv"
brandSrc = csv.reader(open(brandInfoFile, 'r'))
i = 0   # 跳过标题栏
for row in brandSrc:
    if i == 0:
        i = i + 1
        continue
    row[5] = float(row[5])
    if row[5] >= brandBuyLimitNum:
        brandList.append(row[0])

for brand in brandList:
    # 寻找品牌购买前的最大浏览时间和最小浏览时间
    brandMinViewTime = 0
    brandMaxViewTime = 0

    userInfoFile = "userFeatureOfCate" + str(cate) + ".csv"
    userInfo = csv.reader(open(userInfoFile, 'r'))

    i = 0
    for row in userInfo:
        if row[2] == "True" and row[7] != "0" and row[1] == brand:
            row[32] = math.floor(float(row[32]))
            if i == 0:
                i = i + 1
                brandMinViewTime = row[32]
                brandMaxViewTime = row[32]
                continue

            if 0 <= row[32] < brandMinViewTime:
                brandMinViewTime = row[32]
                continue

            if row[32] > brandMaxViewTime:
                brandMaxViewTime = row[32]
                continue
    if brandMaxViewTime > 3600:
        brandMaxViewTime = 3600

    columnNum = 100
    eachGap = 1
    if brandMaxViewTime - brandMinViewTime >= columnNum:
        eachGap = math.floor((brandMaxViewTime - brandMinViewTime) / columnNum)
    else:
        columnNum = brandMaxViewTime - brandMinViewTime + 1

    if brandMaxViewTime > 0:

        userInfo = csv.reader(open(userInfoFile, 'r'))
        buyViewNumList = [0] * columnNum
        for row in userInfo:
            if row[2] == "True" and row[7] != "0" and row[1] == brand:
                row[32] = math.floor(float(row[32]))
                targetColumn = int(math.floor((row[32] - brandMinViewTime) / eachGap))
                if targetColumn >= columnNum:
                    targetColumn = columnNum - 1
                buyViewNumList[targetColumn] = buyViewNumList[targetColumn] + 1

        xTimeAxis = [" "]
        iterPara = brandMinViewTime
        i = 0
        while iterPara < brandMaxViewTime:
            xTimeAxis.append(str(iterPara / 60) + "min")
            iterPara = iterPara + majorGap * eachGap
        if brandMaxViewTime == 3600:
            xTimeAxis.append("60.0min")
        xList = list(range(columnNum))

        fig = plt.figure(figsize=(9.6, 5.4))
        # 不画折线图的原因是有大量的0
        plt.bar(xList, buyViewNumList)

        ax = fig.add_subplot(1, 1, 1)
        ax.set_xticklabels(xTimeAxis)
        # 设置主刻度标签的位置,标签文本的格式
        ax.xaxis.set_major_locator(xMajorLocator)
        # 显示次刻度标签的位置,没有标签文本
        ax.xaxis.set_minor_locator(xMinorLocator)
        ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
        ax.set_title("User View Brand " + str(brand) + " Before First Purchase")
        ax.set_xlabel("BrandViewTime")
        ax.set_ylabel("User Number")

        plt.savefig("../FeatureCate" + str(cate) + "/brandViewTimeDistribution/" + str(brand) + "ViewTime.png")