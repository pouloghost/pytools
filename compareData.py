import sys
import re
#把多个文件中相同key的行放到一起，for excel

#从一行中拿到key
def getKey(line):
    full = line.split('\t')[1]
    p = re.compile(r'.*#(\d*)')
    m = p.match(full)
    if m:
        return m.group(1)
    return ''

def getValue(line):
    return line.split('\t')[2]

def readFile(name, getKey, getValue):
    data = {}
    f = open(name)
    lines = f.readlines()

    for line in lines:
        if len(line) < 3:
            continue
        key = getKey(line)
        value = getValue(line)
        print key, '-', value
        data[key] = value

    return data

def merge(datas):
    merge = {}
    povit = datas[0]
    for (k,v) in povit.items():
        merge[k] = [v]

    for data in datas[1:]:
        for (k,v) in data.items():
            if k in merge:
                merge[k].append(v)

    return merge

def combine(item):
    return item[0] + '\t' + '\t'.join(item[1])

def writeFile(name, merge):
    lines = map(combine , merge.items())
    f = open(name, 'w')
    for line in lines:
        f.write(line)
    f.flush()

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'error input'

    #输出文件
    out = sys.argv[1]
    #输入文件
    ins = sys.argv[2:]
    
    datas = []
    for inf in ins:
        datas.append(readFile(inf, getKey, getValue))

    merge = merge(datas)
    writeFile(out, merge)
    
        
