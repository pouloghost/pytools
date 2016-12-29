# coding:utf-8


def key(line):
    # print(line)
    return '\t'.join(line[1:3])


def value(line):
    return line[0]
