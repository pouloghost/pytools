#coding:utf-8

import csv
import sys

def precheck(tmp, indexes):
    for i in range(len(indexes)):
        if -1 == tmp.find('$' + str(i)):
            return False

    return True
        
def readRowsCsv(inf):
    csvfile = file(inf, 'rb')
    rows = []
    for line in csv.reader(csvfile):
        rows.append(line)
    return rows

def extract(rows, tmp, indexes):
    def oneline(row):
        line = tmp
        for i in range(len(indexes)):
            line = line.replace('$' + str(i), row[int(indexes[i])], 1)
        return line
          
    tmps = map(oneline, rows)
    return ''.join(tmps)

def onResult(result):
    print result
    
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'error input'

    #输入文件
    inf = sys.argv[1]
    #输出模板（每行记录一个）
    tmp = sys.argv[2]
    #变量所在row
    indexes = sys.argv[3:]

    if precheck(tmp, indexes):    
        rows = readRowsCsv(inf)

        result = extract(rows, tmp, indexes)

        onResult(result)
    else:
        print tmp
        print indexes
        print 'error tmp'
