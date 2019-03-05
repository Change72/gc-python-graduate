import csv
import math
from pylab import *
from matplotlib.ticker import MultipleLocator

majorGap = 1
xMajorLocator = MultipleLocator(majorGap)  # 将x主刻度标签设置为20的倍数
xMinorLocator = MultipleLocator(1)  # 将x轴次刻度标签设置为5的倍数

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

    columnNum = 6
    userInfoFile = "userFeatureOfCate" + str(cate) + ".csv"
    userInfo = csv.reader(open(userInfoFile, 'r'))

    buyViewNumList = [0] * columnNum
    i = 0
    for row in userInfo:
        if i == 0:
            i = i + 1
            print(row[15])
        if row[2] == "True" and row[7] != "0" and row[1] == brand:
            row[15] = math.floor(float(row[15]))
            if row[15] > 4:
                row[15] = 5
            seq = row[15]
            buyViewNumList[seq] = buyViewNumList[seq] + 1

    xTimeAxis = [" ", "0", "1", "2", "3", "4", ">4"]

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
    ax.set_title("User with Brand " + str(brand) + " Fav to Buy Times Before First Purchase")
    ax.set_xlabel("Fav to Buy Times")
    ax.set_ylabel("User Number")

    plt.savefig("../FeatureCate" + str(cate) + "/FavtoBuyTimesDistribution/" + str(brand) + "PvtoBuyTime.png")
