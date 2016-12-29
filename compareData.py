# coding:utf-8


import sys
import re
from channel import *

# 把多个文件中相同key的行放到一起，for excel


# 从一行中拿到key
def get_key(line):
    full = line[1]
    p = re.compile(r'.*#(\d*)')
    m = p.match(full)
    if m:
        return m.group(1)
    return ''


def get_value(line):
    return line[2]


def read_file(name, key, val):
    data = {}
    f = open(name, encoding='utf-8')
    lines = f.readlines()

    for line in lines:
        parts = line.split('\t')
        k = key(parts)
        v = val(parts)
        data[k] = v

    return data


def merge(datas):
    merge = {}
    povit = datas[0]
    for (k, v) in povit.items():
        merge[k] = [v]

    for data in datas[1:]:
        for (k, v) in data.items():
            if k in merge:
                merge[k].append(v)

    return merge


def combine(item):
    return item[0].replace('\n', '') + '\t' + '\t'.join(item[1])


def write_file(name, merge):
    lines = map(combine, merge.items())
    f = open(name, 'w', encoding='utf-8')
    for line in lines:
        f.write(line)
        f.write('\n')
    f.flush()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('error input')

    # 输出文件
    out = sys.argv[1]
    # 输入文件
    ins = sys.argv[2:]
    
    datas = []
    for inf in ins:
        datas.append(read_file(inf, key, value))

    merge = merge(datas)
    write_file(out, merge)
