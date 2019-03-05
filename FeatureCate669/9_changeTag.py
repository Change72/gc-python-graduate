import csv

cate = 669

userFile = "second_fourth_tryKMeansOfCate" + str(cate) + ".csv"
userTruth = csv.reader(open(userFile, 'r'))

userDirFile = "second_fourth_final_tryKMeansOfCate" + str(cate) + ".csv"

temp = []
i = 0
for row in userTruth:

    if i > 0:
        row.append("T")
        row[15] = float(row[15])
        row[18] = float(row[18])
        row[31] = float(row[31])
        row[32] = float(row[32])
        if row[35] == "False":
            if row[36] == "0" or row[36] == "2":
                if row[15] > 0 and row[18] > 0:
                    row[37] = "F"
                if row[31] == row[32]:
                    row[37] = "F"
                if row[31] < 300 and row[32] < 480:
                    row[37] = "F"

    if i == 0:
        i = i + 1

    uf = open(userDirFile, 'a', newline='')
    uWriter = csv.writer(uf)
    uWriter.writerow(row)
    uf.close()






