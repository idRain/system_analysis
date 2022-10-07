from io import StringIO
import csv


from io import StringIO
import csv


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []

    bounds = []

    for row in reader:
      bounds.append([int(row[0]), int(row[1])])

    levels = [[1]]
    index = 0
    while index < len(levels):
      level = []
      for x in levels[index]:
        for pair in bounds:
          if pair[0] == x:
            level.append(pair[1])
      if len(level) > 0:
        levels.append(level)
      index += 1


    arr_r1 = []
    for x in bounds:
        if x[0] not in arr_r1:
            arr_r1.append(x[0])

    arr_r2 = []
    for x in bounds:
        if x[1] not in arr_r2:
            arr_r2.append(x[1])

    arr_r3 = []
    for i in range(0, len(levels) - 2):
      arr_r3 += levels[i]

    arr_r4 = []
    for i in range(2, len(levels)):
      arr_r4 += levels[i]

    arr_r5 = []
    for level in levels:
      if len(level) > 1:
        arr_r5 += level

    return [arr_r1, arr_r2, arr_r3, arr_r4, arr_r5]
