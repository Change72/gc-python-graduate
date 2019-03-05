import csv

f = open('userListOfBrand.txt', 'r')
a = f.read()
brandInfo = eval(a)
f.close()

temp = []
for brand in brandInfo:
    print(brand)
    temp.append(brand)

print(len(temp))