import csv

cate = 4263
userInfoFile = "userFeatureOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userInfoFile, 'r'))

trueUserList = []

for row in userInfo:
    if row[2] == "True":
        if row[0] not in trueUserList:
            trueUserList.append(row[0])

srcFile = "userCate" + str(cate) + ".csv"
srcInfo = csv.reader(open(srcFile, 'r'))

dirFile = "trueUserBuyTimestamp" + str(cate) + ".csv"
dirWriter = csv.writer(open(dirFile, 'a', newline=''))
dirWriter.writerow(['user', 'time', 'brand'])

for row in srcInfo:
    if row[1] in trueUserList and row[3] == 'buy':
        dirFile = "trueUserBuyTimestamp" + str(cate) + ".csv"
        dirWriter = csv.writer(open(dirFile, 'a', newline=''))
        dirWriter.writerow([row[1], row[2], row[5]])



