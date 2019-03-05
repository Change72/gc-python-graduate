import csv

cate = 669

# brandBuyLimitNum = 10
# brandList = []
# brandInfoFile = "brandFeatureOfCate" + str(cate) + ".csv"
# brandSrc = csv.reader(open(brandInfoFile, 'r'))
#
# i = 0   # 跳过标题栏
# for row in brandSrc:
#     if i == 0:
#         i = i + 1
#         continue
#     row[5] = float(row[5])
#     if row[5] >= brandBuyLimitNum:
#         brandList.append(row[0])
#
# for brand in brandList:
userInfoFile = "userFeatureOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userInfoFile, 'r'))

userFile = "giveTagOfCate" + str(cate) + ".csv"
# 写入标题
# 用户行为记录 # 35列
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
                      'user_BrandViewTime', 'user_CateViewTime', 'user_ReBuyBrandViewTime',
                      'user_ReBuyCateViewTime', 'user_GiveTag']

# 记录用户行为信息
uf = open(userFile, 'a', newline='')
uWriter = csv.writer(uf)
uWriter.writerow(user_FeatureRecord)
uf.close()

i = 0
for row in userInfo:
    if row[2] == "True" and row[7] != "0":
        # row.remove(row[2])
        # row.remove(row[3])
        row[25] = float(row[25])
        row[26] = float(row[26])
        row[27] = float(row[27])

        row[29] = float(row[29])
        row[30] = float(row[30])

        row.append("False")

        if row[5] == "0" and row[6] == "0":     # row[15] row[16]
            row[35] = "True"
        if row[25] > 7200:
            row[35] = "True"
        if row[26] < 0:
            row[35] = "True"
        if row[27] < 0:
            row[35] = "True"

        if row[29] < 0:
            row[29] = 0
        if row[30] < 0:
            row[30] = 0

        # 7. 记录用户行为信息
        uf = open(userFile, 'a', newline='')
        uWriter = csv.writer(uf)
        uWriter.writerow(row)
        uf.close()
