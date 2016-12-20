import sys
#列数据转成行数据
def readFile(name):
    lines = []
    f = open(name)
    flines = f.readlines()

    step = len(flines)
    
    if 0 != step%3:
        return lines

    i = 0
    step /=3

    total = range(step)
    for i in total:
        one = [flines[i][:-1], flines[i+step][:-1], flines[i+2*step][:-1]]
        line = '\t'.join(one) + '\r\n'
        lines.append(line)

    return lines

def writeFile(name, liness):
    f = open(name, 'w')
    for lines in liness:
        for line in lines:
            f.write(line)
    f.flush()
              
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'error input'
        
    out = sys.argv[1]
    ins = sys.argv[2:]
    
    liness = []
    for inf in ins:
        liness.append(readFile(inf))

    writeFile(out, liness)
    
