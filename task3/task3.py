from io import StringIO
import csv


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []

    bounds = []

    for row in reader:
      bounds.append([int(row[0]), int(row[1])])

    arr_r1 = []
    for x in bounds:
        if x[0] not in arr_r1:
            arr_r1.append(x[0])

    arr_r2 = []
    for x in bounds:
        if x[1] not in arr_r2:
            arr_r2.append(x[1])

    arr_r3 = []
    for x in bounds:
        for y in bounds:
            if x[0] not in arr_r3 and x[1] == y[0]:
                arr_r3.append(x[0])

    arr_r4 = []
    for x in bounds:
        for y in bounds:
            if y[1] not in arr_r4 and x[1] == y[0]:
                arr_r4.append(y[1])

    arr_r5 = []
    for x in bounds:
        for y in bounds:
            if x[1] not in arr_r5 and x[0] == y[0] and x[1] != y[1]:
                arr_r5.append(x[1])
  
    return [arr_r1, arr_r2, arr_r3, arr_r4, arr_r5]
