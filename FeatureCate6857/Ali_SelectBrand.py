import csv

cate = 6857
srcFile = "/root/pythonFile/FeatureCate" + str(cate) + "/userCate" + str(cate) + ".csv"

csvReader = csv.reader(open(srcFile, 'r'))

# claim
brandList = []
brandOfUserList = {}

for row in csvReader:
    if row[5] in brandList:
        if row[1] in brandOfUserList[row[5]]:
            continue
        else:
            brandOfUserList[row[5]].append(row[1])
    else:
        brandList.append(row[5])
        brandOfUserList.setdefault(row[5], [])
        brandOfUserList[row[5]].append(row[1])

dirFile = "/root/pythonFile/FeatureCate" + str(cate) + "/userListOfBrand.txt"
f = open(dirFile, 'w')
f.write(str(brandOfUserList))
f.close()