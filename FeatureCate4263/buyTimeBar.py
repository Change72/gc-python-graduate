import csv
import time
from pylab import *
from matplotlib.ticker import MultipleLocator

xMajorLocator = MultipleLocator(24)  # 将x主刻度标签设置为24的倍数
xMinorLocator = MultipleLocator(6)  # 将x轴次刻度标签设置为6的倍数

cate = 4263
brandInfoFile = "userListOfBrand.txt"
brandReader = open(brandInfoFile, 'r').read()
brandInfo = eval(brandReader)

for brand in brandInfo:

    # 寻找品牌的最大购买时间和最小购买时间
    brandMinBuyTimestamp = 0
    brandMaxBuyTimestamp = 0

    trueUserFile = "trueUserBuyTimestamp" + str(cate) + ".csv"
    userInfo = csv.reader(open(trueUserFile, 'r'))

    i = 0
    for row in userInfo:
        if row[2] == brand:
            row[1] = float(row[1])
            if i == 0:
                i = i + 1
                brandMinBuyTimestamp = row[1]
                brandMaxBuyTimestamp = row[1]
                continue

            if 0 < row[1] < brandMinBuyTimestamp:
                brandMinBuyTimestamp = row[1]
                continue

            if row[1] > brandMaxBuyTimestamp:
                brandMaxBuyTimestamp = row[1]
                continue

    # 有些品牌没有购买记录
    if brandMinBuyTimestamp != 0:
        # 最大最小时间取整到整数天
        hourUnit = 3600
        dayUnit = 24 * 3600

        # 由于时间戳起始为1970 年 1 月 1 日（08:00:00）所以这里需要减8小时才时0点的时间戳
        startTime = math.floor(brandMinBuyTimestamp / dayUnit) * dayUnit - 8 * hourUnit
        endTime = math.ceil(brandMaxBuyTimestamp / dayUnit) * dayUnit - 8 * hourUnit

        xTimeAxis = [" "]     # 插入首个标签，没用，占位
        timeGap = endTime - startTime
        length = int(timeGap / hourUnit)
        dayLength = int(length / 24)
        dayHourList = list(range(length))

        iterPara = startTime
        while iterPara <= endTime:
            if iterPara == startTime or iterPara == endTime:
                timeArray = time.localtime(iterPara)
                minUnitTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
                xTimeAxis.append(minUnitTime)
            else:
                xTimeAxis.append(" ")
            iterPara = iterPara + dayUnit

        trueUserFile = "trueUserBuyTimestamp" + str(cate) + ".csv"
        userInfo = csv.reader(open(trueUserFile, 'r'))

        buyNumList = [0] * length
        for row in userInfo:
            if row[2] == brand:
                timestamp = float(row[1]) - startTime - 8 * hourUnit
                targetColumn = int(math.floor(timestamp / hourUnit))
                buyNumList[targetColumn] = buyNumList[targetColumn] + 1

        dayHourList = list(range(length))
        fig = plt.figure()
        plt.bar(dayHourList, buyNumList)

        ax = fig.add_subplot(1, 1, 1)
        ax.set_xticklabels(xTimeAxis, rotation=5)
        # 设置主刻度标签的位置,标签文本的格式
        ax.xaxis.set_major_locator(xMajorLocator)
        # 显示次刻度标签的位置,没有标签文本
        ax.xaxis.set_minor_locator(xMinorLocator)
        ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
        ax.set_title("User Of Brand " + str(brand) + " Buy Time Distribution")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("Buy Number")

        plt.savefig("../FeatureCate" + str(cate) + "/brandBuyTimeDistribution/" + str(brand) + "BuyTime.png")

