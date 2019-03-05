import csv

cate = 4263

f = open('/root/pythonFile/FeatureCate' + str(cate) + '/userListOfBrand.txt', 'r')
a = f.read()
brandInfo = eval(a)
f.close()

dirFile = '/root/pythonFile/FeatureCate' + str(cate) + '/userCate' + str(cate) + '.csv'
cateFile = '/root/pythonFile/FeatureCate' + str(cate) + '/cateFeatureOfCate' + str(cate) + '.csv'
brandFile = '/root/pythonFile/FeatureCate' + str(cate) + '/brandFeatureOfCate' + str(cate) + '.csv'
userFile = '/root/pythonFile/FeatureCate' + str(cate) + '/userFeatureOfCate' + str(cate) + '.csv'

# 类目层面特征
cate_FeatureRecord = []                     # 类目特征记录表

cate_TransNum = 0                           # 所有与这个类目 正常 交互过的用户量
cate_BrandNum = 0                           # 这个类目下品牌的数量

cate_PvUser = 0                             # 浏览这个类目的用户数
cate_FavUser = 0                            # 收藏这个类目的用户数
cate_CartUser = 0                           # 加购这个类目的用户数
cate_BuyUser = 0                            # 购买这个类目的用户数

cate_PvNum = 0                              # 用户对这个类目的总浏览量
cate_FavNum = 0                             # 用户对这个类目的总收藏量
cate_CartNum = 0                            # 用户对这个类目的总加购量
cate_BuyNum = 0                             # 用户对这个类目的总购买量

cate_ViewPvUser = 0                         # 浏览类目但没有购买的用户数
cate_ViewFavUser = 0                        # 收藏类目但没有购买的用户数
cate_ViewCartUser = 0                       # 加购类目但没有购买的用户数

cate_ReBuyUser = 0                          # 类目的复购用户量
cate_ReBuyNum = 0                           # 类目的复购数量
cate_ReBuyUserRate = 0                      # 类目的用户复购率
cate_ReBuyNumRate = 0                       # 类目的平均复购量
cate_ReBuyTimeGap = 0                       # 类目复购总时间间隔
cate_AverageReBuyTimeGap = 0                # 类目平均复购时间间隔
cate_ReBuyBrandViewTime = 0                 # 品牌用户复购总浏览品牌的时间
cate_ReBuyCateViewTime = 0                  # 品牌用户复购总浏览类目的时间
cate_AverageReBuyBrandViewTime = 0          # 品牌用户复购总浏览品牌的平均时间
cate_AverageReBuyCateViewTime = 0           # 品牌用户复购总浏览类目的平均时间

cate_PvToBuyRate = 0                        # 浏览后购买的用户 转化率
cate_FavToBuyRate = 0                       # 收藏后购买的用户 转化率
cate_CartToBuyRate = 0                      # 加购后购买的用户 转化率

cate_TimesFromPvToBuy = 0                   # 正常用户 购买目标品牌前浏览目标品牌总次数
cate_TimesFromFavToBuy = 0                  # 正常用户 购买目标品牌前收藏目标品牌总次数
cate_TimesFromCartToBuy = 0                 # 正常用户 购买目标品牌前加购目标品牌总次数

cate_AverageTimesFromPvToBuy = 0            # 正常用户 购买目标品牌前平均浏览目标品牌次数
cate_AverageTimesFromFavToBuy = 0           # 正常用户 购买目标品牌前平均收藏目标品牌次数
cate_AverageTimesFromCartToBuy = 0          # 正常用户 购买目标品牌前平均加购目标品牌次数

cate_OtherNumFromPvToBuy = 0                # 正常用户 购买目标品牌前总浏览其他品牌总个数
cate_OtherNumFromFavToBuy = 0               # 正常用户 购买目标品牌前总收藏其他品牌总个数
cate_OtherNumFromCartToBuy = 0              # 正常用户 购买目标品牌前总加购其他品牌总个数
cate_OtherNumFromBuyToBuy = 0               # 正常用户 购买目标品牌前总购买其他品牌总个数

cate_AverageOtherNumFromPvToBuy = 0         # 正常用户 购买目标品牌前平均浏览其他品牌个数
cate_AverageOtherNumFromFavToBuy = 0        # 正常用户 购买目标品牌前平均收藏其他品牌个数
cate_AverageOtherNumFromCartToBuy = 0       # 正常用户 购买目标品牌前平均加购其他品牌个数
cate_AverageOtherNumFromBuyToBuy = 0        # 正常用户 购买目标品牌前平均购买其他品牌个数

cate_OtherTimesFromPvToBuy = 0              # 正常用户 购买目标品牌前浏览其他品牌总次数
cate_OtherTimesFromFavToBuy = 0             # 正常用户 购买目标品牌前收藏其他品牌总次数
cate_OtherTimesFromCartToBuy = 0            # 正常用户 购买目标品牌前加购其他品牌总次数
cate_OtherTimesFromBuyToBuy = 0             # 正常用户 购买目标品牌前购买其他品牌总次数

cate_AverageOtherTimesFromPvToBuy = 0       # 正常用户 购买该品牌前平均浏览其他品牌次数
cate_AverageOtherTimesFromFavToBuy = 0      # 正常用户 购买该品牌前平均收藏其他品牌次数
cate_AverageOtherTimesFromCartToBuy = 0     # 正常用户 购买该品牌前平均加购其他品牌次数
cate_AverageOtherTimesFromBuyToBuy = 0      # 正常用户 购买该品牌前平均购买其他品牌次数

cate_PvToBuyTime = 0                        # 品牌第一次浏览目标品牌到购买目标品牌的总时间
cate_FavToBuyTime = 0                       # 品牌第一次收藏目标品牌到购买目标品牌的总时间
cate_CartToBuyTime = 0                      # 品牌第一次加购目标品牌到购买目标品牌的总时间

cate_AveragePvToBuyTime = 0                 # 品牌第一次浏览品牌到购买目标品牌的平均时间
cate_AverageFavToBuyTime = 0                # 品牌第一次收藏品牌到购买目标品牌的平均时间
cate_AverageCartToBuyTime = 0               # 品牌第一次加购品牌到购买目标品牌的平均时间

cate_CatePvToBuyTime = 0                    # 购买该品牌的用户第一次浏览类目到购买目标品牌的总时间
cate_CateFavToBuyTime = 0                   # 购买该品牌的用户第一次收藏类目到购买目标品牌的总时间
cate_CateCartToBuyTime = 0                  # 购买该品牌的用户第一次加购类目到购买目标品牌的总时间

cate_CateAveragePvToBuyTime = 0             # 购买该品牌的用户第一次浏览类目到购买目标品牌的平均时间
cate_CateAverageFavToBuyTime = 0            # 购买该品牌的用户第一次收藏类目到购买目标品牌的平均时间
cate_CateAverageCartToBuyTime = 0           # 购买该品牌的用户第一次加购类目到购买目标品牌的平均时间

cate_BrandViewTime = 0                      # 购买该品牌的用户第一次购买该品牌前浏览该品牌总时间
cate_CateViewTime = 0                       # 购买该品牌的用户第一次购买该品牌前浏览类目总时间

cate_AverageBrandViewTime = 0               # 购买该品牌的用户第一次购买该品牌前浏览该品牌平均时间
cate_AverageCateViewTime = 0                # 购买该品牌的用户第一次购买该品牌前浏览类目平均时间

cate_FraudUserNum = 0                       # 品牌异常用户数量
cate_FraudBuyNum = 0                        # 品牌异常购买数量
cate_FraudUserRate = 0                      # 品牌异常用户比率
cate_FraudNumRate = 0                       # 品牌平均异常购买量

# 写入标题
# 类目特征记录 # 45列
cate_FeatureRecord = ['cate', 'cate_TransNum', 'cate_BrandNum',
                      'cate_PvUser', 'cate_FavUser', 'cate_CartUser', 'cate_BuyUser',
                      'cate_PvNum', 'cate_FavNum', 'cate_CartNum', 'cate_BuyNum',
                      'cate_ViewPvUser', 'cate_ViewFavUser', 'cate_ViewCartUser',
                      'cate_ReBuyUser', 'cate_ReBuyNum', 'cate_ReBuyUserRate', 'cate_ReBuyNumRate',
                      'cate_AverageReBuyTimeGap', 'cate_PvToBuyRate', 'cate_FavToBuyRate', 'cate_CartToBuyRate',
                      'cate_AverageTimesFromPvToBuy', 'cate_AverageTimesFromFavToBuy',
                      'cate_AverageTimesFromCartToBuy',
                      'cate_AverageOtherNumFromPvToBuy', 'cate_AverageOtherNumFromFavToBuy',
                      'cate_AverageOtherNumFromCartToBuy', 'cate_AverageOtherNumFromBuyToBuy',
                      'cate_AverageOtherTimesFromPvToBuy', 'cate_AverageOtherTimesFromFavToBuy',
                      'cate_AverageOtherTimesFromCartToBuy', 'cate_AverageOtherTimesFromBuyToBuy',
                      'cate_AveragePvToBuyTime', 'cate_AverageFavToBuyTime', 'cate_AverageCartToBuyTime',
                      'cate_CateAveragePvToBuyTime', 'cate_CateAverageFavToBuyTime',
                      'cate_CateAverageCartToBuyTime',
                      'cate_AverageBrandViewTime', 'cate_AverageCateViewTime',
                      'cate_FraudUserNum', 'cate_FraudBuyNum', 'cate_FraudUserRate', 'cate_FraudNumRate',
                      'cate_AverageReBuyBrandViewTime', 'cate_AverageReBuyCateViewTime']

# 保存信息
cf = open(cateFile, 'a', newline='')
cWriter = csv.writer(cf)
cWriter.writerow(cate_FeatureRecord)
cf.close()

# 写入标题
# 品牌特征记录 # 46列
brand_FeatureRecord = ['brand', 'brand_TransNum',
                       'brand_PvUser', 'brand_FavUser', 'brand_CartUser', 'brand_BuyUser',
                       'brand_PvNum', 'brand_FavNum', 'brand_CartNum', 'brand_BuyNum',
                       'brand_ViewPvUser', 'brand_ViewFavUser', 'brand_ViewCartUser',
                       'brand_ReBuyUser', 'brand_ReBuyNum', 'brand_ReBuyUserRate', 'brand_ReBuyNumRate',
                       'brand_AverageReBuyTimeGap',
                       'brand_PvToBuyRate', 'brand_FavToBuyRate', 'brand_CartToBuyRate',
                       'brand_AverageTimesFromPvToBuy', 'brand_AverageTimesFromFavToBuy',
                       'brand_AverageTimesFromCartToBuy',
                       'brand_AverageOtherNumFromPvToBuy', 'brand_AverageOtherNumFromFavToBuy',
                       'brand_AverageOtherNumFromCartToBuy', 'brand_AverageOtherNumFromBuyToBuy',
                       'brand_AverageOtherTimesFromPvToBuy', 'brand_AverageOtherTimesFromFavToBuy',
                       'brand_AverageOtherTimesFromCartToBuy', 'brand_AverageOtherTimesFromBuyToBuy',
                       'brand_AveragePvToBuyTime', 'brand_AverageFavToBuyTime', 'brand_AverageCartToBuyTime',
                       'brand_CateAveragePvToBuyTime', 'brand_CateAverageFavToBuyTime',
                       'brand_CateAverageCartToBuyTime',
                       'brand_AverageBrandViewTime', 'brand_AverageCateViewTime',
                       'brand_FraudUserNum', 'brand_FraudBuyNum', 'brand_FraudUserRate', 'brand_FraudNumRate',
                       'brand_AverageReBuyBrandViewTime', 'brand_AverageReBuyCateViewTime']

# 保存品牌信息
bf = open(brandFile, 'a', newline='')
bWriter = csv.writer(bf)
bWriter.writerow(brand_FeatureRecord)
bf.close()

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
                      'user_BrandViewTime', 'user_CateViewTime', 'user_ReBuyBrandViewTime', 'user_ReBuyCateViewTime']

# 记录用户行为信息
uf = open(userFile, 'a', newline='')
uWriter = csv.writer(uf)
uWriter.writerow(user_FeatureRecord)
uf.close()

#  遍历字典，value值不重复
for brand in brandInfo:

    # 品牌层面特征
    brand_FeatureRecord = []                    # 品牌特征记录表

    brand_TransNum = 0                          # 所有与这个品牌 正常 交互过的用户量

    brand_PvUser = 0                            # 浏览这个品牌的用户数
    brand_FavUser = 0                           # 收藏这个品牌的用户数
    brand_CartUser = 0                          # 加购这个品牌的用户数
    brand_BuyUser = 0                           # 购买这个品牌的用户数

    brand_PvNum = 0                             # 用户对这个品牌的总浏览量
    brand_FavNum = 0                            # 用户对这个品牌的总收藏量
    brand_CartNum = 0                           # 用户对这个品牌的总加购量
    brand_BuyNum = 0                            # 用户对这个品牌的总购买量

    brand_ViewPvUser = 0                        # 浏览品牌但没有购买的用户数
    brand_ViewFavUser = 0                       # 收藏品牌但没有购买的用户数
    brand_ViewCartUser = 0                      # 加购品牌但没有购买的用户数

    brand_ReBuyUser = 0                         # 品牌的复购用户量
    brand_ReBuyNum = 0                          # 品牌的复购数量
    brand_ReBuyUserRate = 0                     # 品牌的用户复购率
    brand_ReBuyNumRate = 0                      # 品牌平均复购数量
    brand_ReBuyTimeGap = 0                      # 品牌第一次购买到第二次总时间
    brand_AverageReBuyTimeGap = 0               # 品牌第一次购买到第二次平均时间间隔
    brand_ReBuyBrandViewTime = 0                # 品牌用户复购总浏览品牌的时间
    brand_ReBuyCateViewTime = 0                 # 品牌用户复购总浏览类目的时间
    brand_AverageReBuyBrandViewTime = 0         # 品牌用户复购总浏览品牌的平均时间
    brand_AverageReBuyCateViewTime = 0          # 品牌用户复购总浏览类目的平均时间

    brand_PvToBuyRate = 0                       # 浏览后购买的用户 转化率
    brand_FavToBuyRate = 0                      # 收藏后购买的用户 转化率
    brand_CartToBuyRate = 0                     # 加购后购买的用户 转化率

    brand_TimesFromPvToBuy = 0                  # 正常用户 购买目标品牌前浏览目标品牌总次数
    brand_TimesFromFavToBuy = 0                 # 正常用户 购买目标品牌前收藏目标品牌总次数
    brand_TimesFromCartToBuy = 0                # 正常用户 购买目标品牌前加购目标品牌总次数

    brand_AverageTimesFromPvToBuy = 0           # 正常用户 购买目标品牌前平均浏览目标品牌次数
    brand_AverageTimesFromFavToBuy = 0          # 正常用户 购买目标品牌前平均收藏目标品牌次数
    brand_AverageTimesFromCartToBuy = 0         # 正常用户 购买目标品牌前平均加购目标品牌次数

    brand_OtherNumFromPvToBuy = 0               # 正常用户 购买目标品牌前总浏览其他品牌总个数
    brand_OtherNumFromFavToBuy = 0              # 正常用户 购买目标品牌前总收藏其他品牌总个数
    brand_OtherNumFromCartToBuy = 0             # 正常用户 购买目标品牌前总加购其他品牌总个数
    brand_OtherNumFromBuyToBuy = 0              # 正常用户 购买目标品牌前总购买其他品牌总个数

    brand_AverageOtherNumFromPvToBuy = 0        # 正常用户 购买目标品牌前平均浏览其他品牌个数
    brand_AverageOtherNumFromFavToBuy = 0       # 正常用户 购买目标品牌前平均收藏其他品牌个数
    brand_AverageOtherNumFromCartToBuy = 0      # 正常用户 购买目标品牌前平均加购其他品牌个数
    brand_AverageOtherNumFromBuyToBuy = 0       # 正常用户 购买目标品牌前平均购买其他品牌个数

    brand_OtherTimesFromPvToBuy = 0             # 正常用户 购买目标品牌前浏览其他品牌总次数
    brand_OtherTimesFromFavToBuy = 0            # 正常用户 购买目标品牌前收藏其他品牌总次数
    brand_OtherTimesFromCartToBuy = 0           # 正常用户 购买目标品牌前加购其他品牌总次数
    brand_OtherTimesFromBuyToBuy = 0            # 正常用户 购买目标品牌前购买其他品牌总次数

    brand_AverageOtherTimesFromPvToBuy = 0      # 正常用户 购买该品牌前平均浏览其他品牌次数
    brand_AverageOtherTimesFromFavToBuy = 0     # 正常用户 购买该品牌前平均收藏其他品牌次数
    brand_AverageOtherTimesFromCartToBuy = 0    # 正常用户 购买该品牌前平均加购其他品牌次数
    brand_AverageOtherTimesFromBuyToBuy = 0     # 正常用户 购买该品牌前平均购买其他品牌次数

    brand_PvToBuyTime = 0                       # 品牌第一次浏览目标品牌到购买目标品牌的总时间
    brand_FavToBuyTime = 0                      # 品牌第一次收藏目标品牌到购买目标品牌的总时间
    brand_CartToBuyTime = 0                     # 品牌第一次加购目标品牌到购买目标品牌的总时间

    brand_AveragePvToBuyTime = 0                # 品牌第一次浏览品牌到购买目标品牌的平均时间
    brand_AverageFavToBuyTime = 0               # 品牌第一次收藏品牌到购买目标品牌的平均时间
    brand_AverageCartToBuyTime = 0              # 品牌第一次加购品牌到购买目标品牌的平均时间

    brand_CatePvToBuyTime = 0                   # 购买该品牌的用户第一次浏览类目到购买目标品牌的总时间
    brand_CateFavToBuyTime = 0                  # 购买该品牌的用户第一次收藏类目到购买目标品牌的总时间
    brand_CateCartToBuyTime = 0                 # 购买该品牌的用户第一次加购类目到购买目标品牌的总时间

    brand_CateAveragePvToBuyTime = 0            # 购买该品牌的用户第一次浏览类目到购买目标品牌的平均时间
    brand_CateAverageFavToBuyTime = 0           # 购买该品牌的用户第一次收藏类目到购买目标品牌的平均时间
    brand_CateAverageCartToBuyTime = 0          # 购买该品牌的用户第一次加购类目到购买目标品牌的平均时间

    brand_BrandViewTime = 0                     # 购买该品牌的用户第一次购买该品牌前浏览该品牌总时间
    brand_CateViewTime = 0                      # 购买该品牌的用户第一次购买该品牌前浏览类目总时间

    brand_AverageBrandViewTime = 0              # 购买该品牌的用户第一次购买该品牌前浏览该品牌平均时间
    brand_AverageCateViewTime = 0               # 购买该品牌的用户第一次购买该品牌前浏览类目平均时间

    brand_FraudUserNum = 0                      # 品牌异常用户数量
    brand_FraudBuyNum = 0                       # 品牌异常购买数量
    brand_FraudUserRate = 0                     # 品牌异常用户比率
    brand_FraudNumRate = 0                      # 品牌平均异常购买量

    for user in brandInfo[brand]:

        # 用户层面特征
        user_FeatureRecord = []             # 用户特征记录表

        user_BehaviorRecord = []            # 用户行为记录

        user_BrandPv = 0                    # 用户对这个品牌的总浏览量
        user_BrandFav = 0                   # 用户对这个品牌的总收藏量
        user_BrandCart = 0                  # 用户对这个品牌的总加购量
        user_BrandBuy = 0                   # 用户对这个品牌的总购买量

        user_CatePv = 0                     # 用户对这个类目的总浏览量
        user_CateFav = 0                    # 用户对这个类目的总收藏量
        user_CateCart = 0                   # 用户对这个类目的总加购量
        user_CateBuy = 0                    # 用户对这个类目的总购买量

        user_ReBuyNum = 0                   # 用户的复购数量
        user_FirstReBuyTimestamp = 0        # 用户第一次复购的时间
        user_ReBuyTimeGap = 0               # 用户从上次购买到本次购买的时间间隔
        user_ReBuyBrandViewTime = 0         # 用户复购总浏览品牌时间
        user_AverageReBuyBrandViewTime = 0  # 用户复购平均浏览品牌时间
        user_ReBuyCateViewTime = 0          # 用户复购总浏览类目时间
        user_AverageReBuyCateViewTime = 0   # 用户复购平均浏览类目时间

        user_TimesFromPvToBuy = 0           # 正常用户 购买目标品牌前浏览目标品牌次数
        user_TimesFromFavToBuy = 0          # 正常用户 购买目标品牌前收藏目标品牌次数
        user_TimesFromCartToBuy = 0         # 正常用户 购买目标品牌前加购目标品牌次数

        user_OtherBrandPvList = []          # 正常用户 购买目标品牌前浏览其他品牌的品牌列表
        user_OtherBrandFavList = []         # 正常用户 购买目标品牌前收藏其他品牌的品牌列表
        user_OtherBrandCartList = []        # 正常用户 购买目标品牌前加购其他品牌的品牌列表
        user_OtherBrandBuyList = []         # 正常用户 购买目标品牌前购买其他品牌的品牌列表

        user_OtherNumFromPvToBuy = 0        # 正常用户 购买目标品牌前浏览其他品牌个数
        user_OtherNumFromFavToBuy = 0       # 正常用户 购买目标品牌前收藏其他品牌个数
        user_OtherNumFromCartToBuy = 0      # 正常用户 购买目标品牌前加购其他品牌个数
        user_OtherNumFromBuyToBuy = 0       # 正常用户 购买目标品牌前购买其他品牌个数

        user_OtherTimesFromPvToBuy = 0      # 正常用户 购买目标品牌前浏览其他品牌次数
        user_OtherTimesFromFavToBuy = 0     # 正常用户 购买目标品牌前收藏其他品牌次数
        user_OtherTimesFromCartToBuy = 0    # 正常用户 购买目标品牌前加购其他品牌次数
        user_OtherTimesFromBuyToBuy = 0     # 正常用户 购买目标品牌前加购其他品牌次数

        user_BrandPvToBuyTime = 0           # 用户第一次浏览该品牌到购买目标品牌的时间
        user_BrandFavToBuyTime = 0          # 用户第一次收藏该品牌到购买目标品牌的时间
        user_BrandCartToBuyTime = 0         # 用户第一次加购该品牌到购买目标品牌的时间

        user_CatePvToBuyTime = 0            # 用户第一次浏览类目到购买目标品牌的时间
        user_CateFavToBuyTime = 0           # 用户第一次收藏类目到购买目标品牌的时间
        user_CateCartToBuyTime = 0          # 用户第一次加购类目到购买目标品牌的时间

        user_BrandViewTime = 0              # 用户下单前浏览目标品牌时间
        user_CateViewTime = 0               # 用户下单前浏览类目的时间

        user_FraudBuyNum = 0                # 用户异常购买数量

        user_FirstBrandTransTimestamp = 0   # 用户第一次与这个品牌交互的时间
        user_FirstCateTransTimestamp = 0    # 用户第一次与这个类目交互的时间

        user_FirstCatePvTimestamp = 0       # 用户第一次浏览这个类目的时间
        user_FirstCateFavTimestamp = 0      # 用户第一次收藏这个类目的时间
        user_FirstCateCartTimestamp = 0     # 用户第一次加购这个类目的时间
        user_FirstCateBuyTimestamp = 0      # 用户第一次购买这个类目的时间

        user_FirstBrandPvTimestamp = 0      # 用户第一次浏览这个品牌的时间
        user_FirstBrandFavTimestamp = 0     # 用户第一次收藏这个品牌的时间
        user_FirstBrandCartTimestamp = 0    # 用户第一次加购这个品牌的时间
        user_FirstBrandBuyTimestamp = 0     # 用户第一次购买这个品牌的时间

        user_Truthful = True                # 用户是否存在异常，True为正常，False为异常

        user_LastCateTransTimestamp = 0     # 用户上一次类目交互的时间戳
        user_LastCateTransBehavior = ''     # 用户上一次类目交互的行为
        user_LastCateTransBrand = 0         # 用户上一次类目交互的品牌

        user_LastBrandTransTimestamp = 0    # 用户上一次品牌交互的时间戳
        user_LastBrandTransBehavior = ''    # 用户上一次品牌交互的行为
        user_LastBrandTransBrand = 0        # 用户上一次品牌交互的品牌

        # 1. 从文件中抽取用户行为
        csvReader = csv.reader(open(dirFile, 'r'))
        for row in csvReader:
            if row[1] == user:
                # 建立行为列表
                user_BehaviorRecord.append(row)

        # 2. 将指定用户行为按时间戳排序
        user_BehaviorRecord = sorted(user_BehaviorRecord, key=lambda x: x[2])

        # 3. 遍历用户行为，更新信息
        i = 0
        tag = True
        for row in user_BehaviorRecord:
            row[2] = float(row[2])
            i = i + 1
            # 3.1 更新首次与类目交互的时间
            if user_FirstCateTransTimestamp == 0:
                user_FirstCateTransTimestamp = row[2]
            # 3.2 更新首次与品牌交互的时间
            if user_FirstBrandTransTimestamp == 0 and row[5] == brand:
                user_FirstBrandTransTimestamp = row[2]
            # 3.3 时间维度上去重
            if i > 1:
                # 时间戳完全重合，去掉
                if row[2] == user_LastCateTransTimestamp:
                    continue
                # 去除5s内的重复操作
                if row[2] - user_LastCateTransTimestamp < 5 and row[3] == user_LastCateTransBehavior:
                    continue
                # 浏览时间统计
                # 距离上一操作小于5min，且还未购买
                if row[2] - user_LastCateTransTimestamp < 300:
                    if user_BrandBuy == 0:
                        user_CateViewTime = user_CateViewTime + row[2] - user_LastCateTransTimestamp
                        if user_LastCateTransBrand == brand:
                            user_BrandViewTime = user_BrandViewTime + row[2] - user_LastCateTransTimestamp
                    elif user_LastCateTransBehavior != 'buy':
                        user_ReBuyCateViewTime = user_ReBuyCateViewTime + row[2] - user_LastCateTransTimestamp
                        if user_LastCateTransBrand == brand:
                            user_ReBuyBrandViewTime = user_ReBuyBrandViewTime + row[2] - user_LastCateTransTimestamp

            # 3.4 操作行为数量角度
            if row[3] == 'pv':
                user_CatePv = user_CatePv + 1
                if user_FirstCatePvTimestamp == 0:
                    user_FirstCatePvTimestamp = row[2]
                if row[5] == brand:
                    user_BrandPv = user_BrandPv + 1
                    # 第一次浏览的时间戳
                    if user_FirstBrandPvTimestamp == 0:
                        user_FirstBrandPvTimestamp = row[2]
                    # 记录购买前的浏览次数
                    if user_BrandBuy == 0:
                        user_TimesFromPvToBuy = user_BrandPv
                else:
                    if user_BrandBuy == 0:
                        user_OtherTimesFromPvToBuy = user_CatePv - user_BrandPv
                        if row[5] not in user_OtherBrandPvList:
                            user_OtherBrandPvList.append(row[5])

            elif row[3] == 'fav':
                user_CateFav = user_CateFav + 1
                if user_FirstCateFavTimestamp == 0:
                    user_FirstCateFavTimestamp = row[2]
                if row[5] == brand:
                    user_BrandFav = user_BrandFav + 1
                    if user_FirstBrandFavTimestamp == 0:
                        user_FirstBrandFavTimestamp = row[2]
                    # 记录购买前的收藏次数
                    if user_BrandBuy == 0:
                            user_TimesFromFavToBuy = user_BrandFav
                else:
                    if user_BrandBuy == 0:
                        user_OtherTimesFromFavToBuy = user_CateFav - user_BrandFav
                        if row[5] not in user_OtherBrandFavList:
                            user_OtherBrandFavList.append(row[5])

            elif row[3] == 'cart':
                user_CateCart = user_CateCart + 1
                if user_FirstCateCartTimestamp == 0:
                    user_FirstCateCartTimestamp = row[2]
                if row[5] == brand:
                    user_BrandCart = user_BrandCart + 1
                    if user_FirstBrandCartTimestamp == 0:
                        user_FirstBrandCartTimestamp = row[2]
                    # 记录购买前的加购次数
                    if user_BrandBuy == 0:
                        user_TimesFromCartToBuy = user_BrandCart
                else:
                    if user_BrandBuy == 0:
                        user_OtherTimesFromCartToBuy = user_CateCart - user_BrandCart
                        if row[5] not in user_OtherBrandCartList:
                            user_OtherBrandCartList.append(row[5])

            elif row[3] == 'buy':
                user_CateBuy = user_CateBuy + 1
                if user_FirstCateBuyTimestamp == 0:
                    user_FirstCateBuyTimestamp = row[2]
                if row[5] == brand:
                    user_BrandBuy = user_BrandBuy + 1
                    if user_FirstBrandBuyTimestamp == 0:
                        user_FirstBrandBuyTimestamp = row[2]
                    # 第二次购买时间
                    if user_BrandBuy == 2:
                        user_FirstReBuyTimestamp = row[2]
                else:
                    if user_BrandBuy == 0:
                        user_OtherTimesFromBuyToBuy = user_CateBuy - user_BrandBuy
                        if row[5] not in user_OtherBrandBuyList:
                            user_OtherBrandBuyList.append(row[5])

            # 3.5 异常用户处理
            # 如果用户与这个品牌的第一次交互即为购买，则列为异常
            if user_FirstBrandTransTimestamp == user_FirstBrandBuyTimestamp \
                    and user_FirstBrandTransTimestamp != 0 and user_BrandBuy == 1 and tag:
                tag = False
                user_Truthful = False
                user_FraudBuyNum = user_FraudBuyNum + 1
            # 如果用户购买这个品牌后的下一次与这个品牌的交互 同为购买，则列为异常
            if user_LastBrandTransBehavior == 'buy' and row[3] == 'buy' and row[5] == brand:
                user_Truthful = False
                user_FraudBuyNum = user_FraudBuyNum + 1

            # 3.6 记录上一次操作的信息
            user_LastCateTransTimestamp = row[2]
            user_LastCateTransBehavior = row[3]
            user_LastCateTransBrand = row[5]

            if row[5] == brand:
                user_LastBrandTransTimestamp = row[2]
                user_LastBrandTransBehavior = row[3]
                user_LastBrandTransBrand = row[5]

        # 4. 正常用户复购
        if user_BrandBuy > 1 and user_Truthful:
            user_ReBuyNum = user_BrandBuy - 1
            user_ReBuyTimeGap = user_FirstReBuyTimestamp - user_FirstBrandBuyTimestamp

            user_AverageReBuyCateViewTime = user_ReBuyCateViewTime / user_ReBuyNum
            user_AverageReBuyBrandViewTime = user_ReBuyBrandViewTime / user_ReBuyNum

            brand_ReBuyUser = brand_ReBuyUser + 1
            brand_ReBuyNum = brand_ReBuyNum + user_ReBuyNum
            brand_ReBuyTimeGap = brand_ReBuyTimeGap + user_ReBuyTimeGap
            brand_ReBuyCateViewTime = brand_ReBuyCateViewTime + user_ReBuyCateViewTime
            brand_ReBuyBrandViewTime = brand_ReBuyBrandViewTime + user_ReBuyBrandViewTime

        # 5. 用户二次特征处理

        # 5.1 与其他店铺交互的个数
        user_OtherNumFromPvToBuy = len(user_OtherBrandPvList)
        user_OtherNumFromFavToBuy = len(user_OtherBrandFavList)
        user_OtherNumFromCartToBuy = len(user_OtherBrandCartList)
        user_OtherNumFromBuyToBuy = len(user_OtherBrandBuyList)

        # 5.2 第一次交互到购买的时间
        if user_BrandBuy != 0:
            #   5.2.1 品牌类
            if user_FirstBrandPvTimestamp < user_FirstBrandBuyTimestamp and user_FirstBrandPvTimestamp != 0:
                user_BrandPvToBuyTime = user_FirstBrandBuyTimestamp - user_FirstBrandPvTimestamp
            else:
                user_Truthful = False

            if user_FirstBrandFavTimestamp != 0:
                user_BrandFavToBuyTime = user_FirstBrandBuyTimestamp - user_FirstBrandFavTimestamp
            if user_FirstBrandCartTimestamp != 0:
                user_BrandCartToBuyTime = user_FirstBrandBuyTimestamp - user_FirstBrandCartTimestamp

            #   5.2.2 类目类
            if user_FirstCatePvTimestamp < user_FirstBrandBuyTimestamp and user_FirstCatePvTimestamp != 0:
                user_CatePvToBuyTime = user_FirstBrandBuyTimestamp - user_FirstCatePvTimestamp
            else:
                user_Truthful = False

            if user_FirstCateFavTimestamp != 0:
                user_CateFavToBuyTime = user_FirstBrandBuyTimestamp - user_FirstCateFavTimestamp
            if user_FirstCateCartTimestamp != 0:
                user_CateCartToBuyTime = user_FirstBrandBuyTimestamp - user_FirstCateCartTimestamp

        # 6. 用户行为记录 # 35列
        user_FeatureRecord = [user, brand, user_Truthful, user_FraudBuyNum,
                              user_BrandPv, user_BrandFav, user_BrandCart, user_BrandBuy,
                              user_CatePv, user_CateFav, user_CateCart, user_CateBuy,
                              user_ReBuyNum, user_ReBuyTimeGap,
                              user_TimesFromPvToBuy, user_TimesFromFavToBuy, user_TimesFromCartToBuy,
                              user_OtherNumFromPvToBuy, user_OtherNumFromFavToBuy, user_OtherNumFromCartToBuy,
                              user_OtherNumFromBuyToBuy, user_OtherTimesFromPvToBuy, user_OtherTimesFromFavToBuy,
                              user_OtherTimesFromCartToBuy, user_OtherTimesFromBuyToBuy,
                              user_BrandPvToBuyTime, user_BrandFavToBuyTime, user_BrandCartToBuyTime,
                              user_CatePvToBuyTime, user_CateFavToBuyTime, user_CateCartToBuyTime,
                              user_BrandViewTime, user_CateViewTime,
                              user_AverageReBuyBrandViewTime, user_AverageReBuyCateViewTime]

        # 7. 记录用户行为信息
        uf = open(userFile, 'a', newline='')
        uWriter = csv.writer(uf)
        uWriter.writerow(user_FeatureRecord)
        uf.close()

        # 8. 异常用户处理
        if not user_Truthful:
            brand_FraudUserNum = brand_FraudUserNum + 1
            brand_FraudBuyNum = brand_FraudBuyNum + user_FraudBuyNum

        # 9. 正常用户处理
        if user_Truthful:
            brand_TransNum = brand_TransNum + 1
            if user_BrandPv != 0:
                brand_PvUser = brand_PvUser + 1
                brand_PvNum = brand_PvNum + user_BrandPv

            if user_BrandFav != 0:
                brand_FavUser = brand_FavUser + 1
                brand_FavNum = brand_FavNum + user_BrandFav

            if user_BrandCart != 0:
                brand_CartUser = brand_CartUser + 1
                brand_CartNum = brand_CartNum + user_BrandCart

            # 9.1 购买了该品牌的用户
            if user_BrandBuy != 0:
                brand_BuyUser = brand_BuyUser + 1
                brand_BuyNum = brand_BuyNum + user_BrandBuy

                brand_TimesFromPvToBuy = brand_TimesFromPvToBuy + user_TimesFromPvToBuy
                brand_TimesFromFavToBuy = brand_TimesFromFavToBuy + user_TimesFromFavToBuy
                brand_TimesFromCartToBuy = brand_TimesFromCartToBuy + user_TimesFromCartToBuy

                brand_OtherNumFromPvToBuy = brand_OtherNumFromPvToBuy + user_OtherNumFromPvToBuy
                brand_OtherNumFromFavToBuy = brand_OtherNumFromFavToBuy + user_OtherNumFromFavToBuy
                brand_OtherNumFromCartToBuy = brand_OtherNumFromCartToBuy + user_OtherNumFromCartToBuy
                brand_OtherNumFromBuyToBuy = brand_OtherNumFromBuyToBuy + user_OtherNumFromBuyToBuy

                brand_OtherTimesFromPvToBuy= brand_OtherTimesFromPvToBuy + user_OtherTimesFromPvToBuy
                brand_OtherTimesFromFavToBuy = brand_OtherTimesFromFavToBuy + user_OtherTimesFromFavToBuy
                brand_OtherTimesFromCartToBuy = brand_OtherTimesFromCartToBuy + user_OtherTimesFromCartToBuy
                brand_OtherTimesFromBuyToBuy = brand_OtherTimesFromBuyToBuy + user_OtherTimesFromBuyToBuy

                brand_PvToBuyTime = brand_PvToBuyTime + user_BrandPvToBuyTime
                brand_FavToBuyTime = brand_FavToBuyTime + user_BrandFavToBuyTime
                brand_CartToBuyTime = brand_CartToBuyTime + user_BrandCartToBuyTime

                brand_CatePvToBuyTime = brand_CatePvToBuyTime + user_CatePvToBuyTime
                brand_CateFavToBuyTime = brand_CateFavToBuyTime + user_CateFavToBuyTime
                brand_CateCartToBuyTime = brand_CateCartToBuyTime + user_CateCartToBuyTime

                brand_BrandViewTime = brand_BrandViewTime + user_BrandViewTime
                brand_CateViewTime = brand_CateViewTime + user_CateViewTime

            # 9.2 未购买的用户
            else:
                if user_BrandPv != 0:
                    brand_ViewPvUser = brand_ViewPvUser + 1

                if user_BrandFav != 0:
                    brand_ViewFavUser = brand_ViewFavUser + 1

                if user_BrandCart != 0:
                    brand_ViewCartUser = brand_ViewCartUser + 1

    # 品牌层面
    if brand_BuyUser != 0:

        if brand_ReBuyUser != 0:
            brand_ReBuyUserRate = brand_ReBuyUser / brand_BuyUser
            brand_ReBuyNumRate = brand_ReBuyNum / brand_ReBuyUser
            brand_AverageReBuyTimeGap = brand_ReBuyTimeGap / brand_ReBuyUser
            brand_AverageReBuyCateViewTime = brand_ReBuyCateViewTime / brand_ReBuyUser
            brand_AverageReBuyBrandViewTime = brand_ReBuyBrandViewTime / brand_ReBuyUser

        if brand_PvUser != 0:
            brand_PvToBuyRate = brand_BuyUser / brand_PvUser
        if brand_FavUser != 0:
            brand_FavToBuyRate = brand_BuyUser / brand_FavUser
        if brand_CartUser != 0:
            brand_CartToBuyRate = brand_BuyUser / brand_CartUser

        brand_AverageTimesFromPvToBuy = brand_TimesFromPvToBuy / brand_BuyUser
        brand_AverageTimesFromFavToBuy = brand_TimesFromFavToBuy / brand_BuyUser
        brand_AverageTimesFromCartToBuy = brand_TimesFromCartToBuy / brand_BuyUser

        brand_AverageOtherNumFromPvToBuy = brand_OtherNumFromPvToBuy / brand_BuyUser
        brand_AverageOtherNumFromFavToBuy = brand_OtherNumFromFavToBuy / brand_BuyUser
        brand_AverageOtherNumFromCartToBuy = brand_OtherNumFromCartToBuy / brand_BuyUser
        brand_AverageOtherNumFromBuyToBuy = brand_OtherNumFromBuyToBuy / brand_BuyUser

        brand_AverageOtherTimesFromPvToBuy = brand_OtherTimesFromPvToBuy / brand_BuyUser
        brand_AverageOtherTimesFromFavToBuy = brand_OtherTimesFromFavToBuy / brand_BuyUser
        brand_AverageOtherTimesFromCartToBuy = brand_OtherTimesFromCartToBuy / brand_BuyUser
        brand_AverageOtherTimesFromBuyToBuy = brand_OtherTimesFromBuyToBuy / brand_BuyUser

        brand_AveragePvToBuyTime = brand_PvToBuyTime / brand_BuyUser
        brand_AverageFavToBuyTime = brand_FavToBuyTime / brand_BuyUser
        brand_AverageCartToBuyTime = brand_CartToBuyTime / brand_BuyUser

        brand_CateAveragePvToBuyTime = brand_CatePvToBuyTime / brand_BuyUser
        brand_CateAverageFavToBuyTime = brand_CateFavToBuyTime / brand_BuyUser
        brand_CateAverageCartToBuyTime = brand_CateCartToBuyTime / brand_BuyUser

        brand_AverageBrandViewTime = brand_BrandViewTime / brand_BuyUser
        brand_AverageCateViewTime = brand_CateViewTime / brand_BuyUser

        if brand_FraudUserNum != 0:
            brand_FraudUserRate = brand_FraudUserNum / (brand_TransNum + brand_FraudUserNum)
            brand_FraudNumRate = brand_FraudBuyNum / brand_FraudUserNum

    # 品牌特征记录 # 46列
    brand_FeatureRecord = [brand, brand_TransNum, brand_PvUser, brand_FavUser, brand_CartUser, brand_BuyUser,
                           brand_PvNum, brand_FavNum, brand_CartNum, brand_BuyNum,
                           brand_ViewPvUser, brand_ViewFavUser, brand_ViewCartUser,
                           brand_ReBuyUser, brand_ReBuyNum, brand_ReBuyUserRate, brand_ReBuyNumRate,
                           brand_AverageReBuyTimeGap, brand_PvToBuyRate, brand_FavToBuyRate, brand_CartToBuyRate,
                           brand_AverageTimesFromPvToBuy, brand_AverageTimesFromFavToBuy,
                           brand_AverageTimesFromCartToBuy,
                           brand_AverageOtherNumFromPvToBuy, brand_AverageOtherNumFromFavToBuy,
                           brand_AverageOtherNumFromCartToBuy, brand_AverageOtherNumFromBuyToBuy,
                           brand_AverageOtherTimesFromPvToBuy, brand_AverageOtherTimesFromFavToBuy,
                           brand_AverageOtherTimesFromCartToBuy, brand_AverageOtherTimesFromBuyToBuy,
                           brand_AveragePvToBuyTime, brand_AverageFavToBuyTime, brand_AverageCartToBuyTime,
                           brand_CateAveragePvToBuyTime, brand_CateAverageFavToBuyTime,
                           brand_CateAverageCartToBuyTime,
                           brand_AverageBrandViewTime, brand_AverageCateViewTime,
                           brand_FraudUserNum, brand_FraudBuyNum, brand_FraudUserRate, brand_FraudNumRate,
                           brand_AverageReBuyBrandViewTime, brand_AverageReBuyCateViewTime]

    # 7. 保存品牌信息
    bf = open(brandFile, 'a', newline='')
    bWriter = csv.writer(bf)
    bWriter.writerow(brand_FeatureRecord)
    bf.close()

    # 8. 品牌特征 -> 类目特征
    cate_TransNum = cate_TransNum + brand_TransNum
    cate_BrandNum = cate_BrandNum + 1

    cate_PvUser = cate_PvUser + brand_PvUser
    cate_FavUser = cate_FavUser + brand_FavUser
    cate_CartUser = cate_CartUser + brand_CartUser
    cate_BuyUser = cate_BuyUser + brand_BuyUser

    cate_PvNum = cate_PvNum + brand_PvNum
    cate_FavNum = cate_FavNum + brand_FavNum
    cate_CartNum = cate_CartNum + brand_CartNum
    cate_BuyNum = cate_BuyNum + brand_BuyNum

    cate_ViewPvUser = cate_ViewPvUser + brand_ViewPvUser
    cate_ViewFavUser = cate_ViewFavUser + brand_ViewFavUser
    cate_ViewCartUser = cate_ViewCartUser + brand_ViewCartUser

    cate_ReBuyUser = cate_ReBuyUser + brand_ReBuyUser
    cate_ReBuyNum = cate_ReBuyNum + brand_ReBuyNum
    cate_ReBuyTimeGap = cate_ReBuyTimeGap + brand_ReBuyTimeGap
    cate_ReBuyBrandViewTime = cate_ReBuyBrandViewTime + brand_ReBuyBrandViewTime
    cate_ReBuyCateViewTime = cate_ReBuyCateViewTime + brand_ReBuyCateViewTime

    cate_TimesFromPvToBuy = cate_TimesFromPvToBuy + brand_TimesFromPvToBuy
    cate_TimesFromFavToBuy = cate_TimesFromFavToBuy + brand_TimesFromFavToBuy
    cate_TimesFromCartToBuy = cate_TimesFromCartToBuy + brand_TimesFromCartToBuy

    cate_OtherNumFromPvToBuy = cate_OtherNumFromPvToBuy + brand_OtherNumFromPvToBuy
    cate_OtherNumFromFavToBuy = cate_OtherNumFromFavToBuy + brand_OtherNumFromFavToBuy
    cate_OtherNumFromCartToBuy = cate_OtherNumFromCartToBuy + brand_OtherNumFromCartToBuy
    cate_OtherNumFromBuyToBuy = cate_OtherNumFromBuyToBuy + brand_OtherNumFromBuyToBuy

    cate_OtherTimesFromPvToBuy = cate_OtherTimesFromPvToBuy + brand_OtherTimesFromPvToBuy
    cate_OtherTimesFromFavToBuy = cate_OtherTimesFromFavToBuy + brand_OtherTimesFromFavToBuy
    cate_OtherTimesFromCartToBuy = cate_OtherTimesFromCartToBuy + brand_OtherTimesFromCartToBuy
    cate_OtherTimesFromBuyToBuy = cate_OtherTimesFromBuyToBuy + brand_OtherTimesFromBuyToBuy

    cate_PvToBuyTime = cate_PvToBuyTime + brand_PvToBuyTime
    cate_FavToBuyTime = cate_FavToBuyTime + brand_FavToBuyTime
    cate_CartToBuyTime = cate_CartToBuyTime + brand_CartToBuyTime

    cate_CatePvToBuyTime = cate_CatePvToBuyTime + brand_CatePvToBuyTime
    cate_CateFavToBuyTime = cate_CateFavToBuyTime + brand_CateFavToBuyTime
    cate_CateCartToBuyTime = cate_CateCartToBuyTime + brand_CateCartToBuyTime

    cate_BrandViewTime = cate_BrandViewTime + brand_BrandViewTime
    cate_CateViewTime = cate_CateViewTime + brand_CateViewTime

    cate_FraudUserNum = cate_FraudUserNum + brand_FraudUserNum
    cate_FraudBuyNum = cate_FraudBuyNum + brand_FraudBuyNum

if cate_BuyUser != 0:

    if cate_ReBuyUser != 0:
        cate_ReBuyUserRate = cate_ReBuyUser / cate_BuyUser
        cate_ReBuyNumRate = cate_ReBuyNum / cate_ReBuyUser
        cate_AverageReBuyTimeGap = cate_ReBuyTimeGap / cate_ReBuyUser
        cate_AverageReBuyBrandViewTime = cate_ReBuyBrandViewTime / cate_ReBuyUser
        cate_AverageReBuyCateViewTime = cate_ReBuyCateViewTime / cate_ReBuyUser

    if cate_PvUser != 0:
        cate_PvToBuyRate = cate_BuyUser / cate_PvUser
    if cate_FavUser != 0:
        cate_FavToBuyRate = cate_BuyUser / cate_FavUser
    if cate_CartUser != 0:
        cate_CartToBuyRate = cate_BuyUser / cate_CartUser

    cate_AverageTimesFromPvToBuy = cate_TimesFromPvToBuy / cate_BuyUser
    cate_AverageTimesFromFavToBuy = cate_TimesFromFavToBuy / cate_BuyUser
    cate_AverageTimesFromCartToBuy = cate_TimesFromCartToBuy / cate_BuyUser

    cate_AverageOtherNumFromPvToBuy = cate_OtherNumFromPvToBuy / cate_BuyUser
    cate_AverageOtherNumFromFavToBuy = cate_OtherNumFromFavToBuy / cate_BuyUser
    cate_AverageOtherNumFromCartToBuy = cate_OtherNumFromCartToBuy / cate_BuyUser
    cate_AverageOtherNumFromBuyToBuy = cate_OtherNumFromBuyToBuy / cate_BuyUser

    cate_AverageOtherTimesFromPvToBuy = cate_OtherTimesFromPvToBuy / cate_BuyUser
    cate_AverageOtherTimesFromFavToBuy = cate_OtherTimesFromFavToBuy / cate_BuyUser
    cate_AverageOtherTimesFromCartToBuy = cate_OtherTimesFromCartToBuy / cate_BuyUser
    cate_AverageOtherTimesFromBuyToBuy = cate_OtherTimesFromBuyToBuy / cate_BuyUser

    cate_AveragePvToBuyTime = cate_PvToBuyTime / cate_BuyUser
    cate_AverageFavToBuyTime = cate_FavToBuyTime / cate_BuyUser
    cate_AverageCartToBuyTime = cate_CartToBuyTime / cate_BuyUser

    cate_CateAveragePvToBuyTime = cate_CatePvToBuyTime / cate_BuyUser
    cate_CateAverageFavToBuyTime = cate_CateFavToBuyTime / cate_BuyUser
    cate_CateAverageCartToBuyTime = cate_CateCartToBuyTime / cate_BuyUser

    cate_AverageBrandViewTime = cate_BrandViewTime / cate_BuyUser
    cate_AverageCateViewTime = cate_CateViewTime / cate_BuyUser

    if cate_FraudUserNum != 0:
        cate_FraudUserRate = cate_FraudUserNum / (cate_TransNum + cate_FraudUserNum)
        cate_FraudNumRate = cate_FraudBuyNum / cate_FraudUserNum

# 类目特征记录 # 45列
cate_FeatureRecord = [cate, cate_TransNum, cate_BrandNum, cate_PvUser, cate_FavUser, cate_CartUser, cate_BuyUser,
                      cate_PvNum, cate_FavNum, cate_CartNum, cate_BuyNum,
                      cate_ViewPvUser, cate_ViewFavUser, cate_ViewCartUser,
                      cate_ReBuyUser, cate_ReBuyNum, cate_ReBuyUserRate, cate_ReBuyNumRate,
                      cate_AverageReBuyTimeGap, cate_PvToBuyRate, cate_FavToBuyRate, cate_CartToBuyRate,
                      cate_AverageTimesFromPvToBuy, cate_AverageTimesFromFavToBuy,
                      cate_AverageTimesFromCartToBuy,
                      cate_AverageOtherNumFromPvToBuy, cate_AverageOtherNumFromFavToBuy,
                      cate_AverageOtherNumFromCartToBuy, cate_AverageOtherNumFromBuyToBuy,
                      cate_AverageOtherTimesFromPvToBuy, cate_AverageOtherTimesFromFavToBuy,
                      cate_AverageOtherTimesFromCartToBuy, cate_AverageOtherTimesFromBuyToBuy,
                      cate_AveragePvToBuyTime, cate_AverageFavToBuyTime, cate_AverageCartToBuyTime,
                      cate_CateAveragePvToBuyTime, cate_CateAverageFavToBuyTime,
                      cate_CateAverageCartToBuyTime,
                      cate_AverageBrandViewTime, cate_AverageCateViewTime,
                      cate_FraudUserNum, cate_FraudBuyNum, cate_FraudUserRate, cate_FraudNumRate,
                      cate_AverageReBuyBrandViewTime, cate_AverageReBuyCateViewTime]

# 7. 保存信息
cf = open(cateFile, 'a', newline='')
cWriter = csv.writer(cf)
cWriter.writerow(cate_FeatureRecord)
cf.close()
