import re

file = 'day4'

xmasFound = 0
with open(file, 'r') as day4file:
    content = day4file.read()
    pattern = 'XMAS'
    count = 0
    line = content.splitlines()
    rowCount = 0
    columnCount = 0
    for row in line:
        for column in row:
            # print (column)
        # print(row[0])
            count += 1
            if count == 5:
                break

            # this is horizontal ->
            if column == 'X':
                if row[columnCount + 1] == 'M':
                    if row[columnCount + 2] == 'A':
                        if row[columnCount + 3] == 'S':
                            xmasFound += 1
            # this is backward
            if column == 'X':
                if row[columnCount - 1] == 'M':
                    if row[columnCount - 2] == 'A':
                        if row[columnCount - 3] == 'S':
                            xmasFound += 1
            # this is diagonal up right
            if column == 'X':
                if line[rowCount-1][columnCount + 1] == 'M':
                    if line[rowCount-2][columnCount + 2] == 'A':
                        if line[rowCount-3][columnCount + 3] == 'S':
                            xmasFound += 1
            # this is diagonal up left
            if column == 'X':
                if line[rowCount-1][columnCount - 1] == 'M':
                    if line[rowCount-2][columnCount - 2] == 'A':
                        if line[rowCount-3][columnCount - 3] == 'S':
                            xmasFound += 1
             # this is diagonal down left
            if column == 'X':
                if line[rowCount+1][columnCount - 1] == 'M':
                    if line[rowCount+2][columnCount - 2] == 'A':
                        if line[rowCount+3][columnCount - 3] == 'S':
                            xmasFound += 1
             # this is diagonal down right
            if column == 'X':
                if line[rowCount+1][columnCount + 1] == 'M':
                    if line[rowCount+2][columnCount + 2] == 'A':
                        if line[rowCount+3][columnCount + 3] == 'S':
                            xmasFound += 1
             # this is down
            if column == 'X':
                if line[rowCount+1][columnCount] == 'M':
                    if line[rowCount+2][columnCount] == 'A':
                        if line[rowCount+3][columnCount] == 'S':
                            xmasFound += 1
            # this is up
            if column == 'X':
                if line[rowCount-1][columnCount] == 'M':
                    if line[rowCount-1][columnCount] == 'A':
                        if line[rowCount-1][columnCount] == 'S':
                            xmasFound += 1
            # print(row[columnCount + 1])
            columnCount += 1
        rowCount += 1
        break



    rowLength = len(line)
    columnLength = len()
    for row in range(rowLength):
        for column in range(columnLength):
            if line[row][column] == 'X':
                