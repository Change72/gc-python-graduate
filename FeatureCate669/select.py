import csv

cate = 669

userInfoFile = "giveTagOfCate" + str(cate) + ".csv"
userInfo = csv.reader(open(userInfoFile, 'r'))

userFile = "second_kMeansOfCate" + str(cate) + ".csv"

i = 0
for row in userInfo:
    if row[35] == "False":
        row.remove(row[35])
        row.remove(row[11])
        row.remove(row[10])
        row.remove(row[9])
        row.remove(row[8])
        row.remove(row[7])
        row.remove(row[6])
        row.remove(row[5])
        row.remove(row[4])
        row.remove(row[3])
        row.remove(row[2])
        row.remove(row[0])

        uf = open(userFile, 'a', newline='')
        uWriter = csv.writer(uf)
        uWriter.writerow(row)
        uf.close()




