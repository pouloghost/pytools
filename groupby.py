# coding:utf-8

import sys
from channel import *


# 模拟sql的groupby


def read_all(inf):
    lines = []
    file = open(inf, encoding='utf-8')
    raws = file.readlines()
    for raw in raws:
        raw = raw
        parts = raw.split('\t')
        lines.append(parts)
    return lines


def on_new_line(kvs, line):
    k = key(line)
    v = value(line)
    v += kvs.get(k, 0)
    kvs[k] = v


def group_by(lines, on_line):
    kvs = {}
    for line in lines:
        on_line(kvs, line)
    return kvs


def out(kvs, outf):
    f = open(outf, 'w', encoding='utf-8')
    items = map(lambda item: [str(item[1]), item[0]], kvs.items())
    lines = map(lambda item: '\t'.join(item), items)
    for line in lines:
        f.write(line)
        f.write('\n')
    f.flush()


if __name__ == '__main__':
    if 3 != len(sys.argv):
        print("error")

    lines = read_all(sys.argv[1])

    kvs = group_by(lines, on_new_line)

    out(kvs, sys.argv[2])
