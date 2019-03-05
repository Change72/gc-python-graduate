import csv

cate = 669
userInfoFile = "userFeatureOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userInfoFile, 'r'))
userFile = "withBrandGiveTagOfCate" + str(cate) + ".csv"

brandInfoFile = "brandFeatureOfCate" + str(cate) + ".csv"
brandInfo = csv.reader(open(brandInfoFile, 'r'))
bigBrandList = []

i = 0
for row in brandInfo:
    if i == 0:
        i = i + 1
        continue

    else:
        row[5] = float(row[5])
        if row[5] > 20:
            bigBrandList.append(row[0])


i = 0
for row in userInfo:
    if i == 0:
        i = i + 1
        row.append("Tag")

        # 记录标题
        uf = open(userFile, 'a', newline='')
        uWriter = csv.writer(uf)
        uWriter.writerow(row)
        uf.close()
        continue
    else:
        if row[2] == "True" and row[7] != "0":
            row[15] = float(row[15])
            row[16] = float(row[16])
            row[18] = float(row[18])
            row[25] = float(row[25])
            row[26] = float(row[26])
            row[27] = float(row[27])
            row[28] = float(row[28])
            row[29] = float(row[29])
            row[30] = float(row[30])
            row[31] = float(row[31])
            row[32] = float(row[32])

            row.append("UnKnown")

            if row[1] not in bigBrandList:
                row[35] = "True"
            if row[15] == 0 and row[16] == 0:     # row[15] row[16]
                row[35] = "True"
            if row[25] > 7200:
                row[35] = "True"
            if row[26] < 0:
                row[35] = "True"
            if row[27] < 0:
                row[35] = "True"

            if row[28] > 432000:
                row[35] = "True"

            if row[35] == "UnKnown":
                if row[31] == row[32] and row[31] < 600:
                    row[35] = "False"

                if row[31] < 300 and row[32] < 480 and row[15] > 0 and row[18] > 0:
                    row[35] = "False"

            # 7. 记录用户行为信息
            uf = open(userFile, 'a', newline='')
            uWriter = csv.writer(uf)
            uWriter.writerow(row)
            uf.close()
