from xml.etree import ElementTree as ET
from sys import argv

#按标准xml，清理其他xml

def readNames(fileName):
    try:
        tree = ET.parse(fileName)
        root = tree.getroot()
    except Exception, e:
        print "error open, ", e
        return None
    
    strings = root.findall('string')
    names = {}
    for string in strings:
        if string.attrib.has_key('name'):
            name = string.attrib['name']
            if not names.has_key(name):
                names[name] = [string, False]
    return names
#填入默认值
def addByFilter(names, root):
    for value in names.itervalues():
        if not value[1]:
            root.append(value[0])
            print value[0]
#删除多余值
def deleteByFilter(names, fileName):
    try:
        tree = ET.parse(fileName)
        root = tree.getroot()
    except Exception, e:
        print "error open, ", e
        return 0

    strings = root.findall('string')
    for string in strings:
        if string.attrib.has_key('name'):
            name = string.attrib['name']
            if not names.has_key(name):
                print name
                root.remove(string)
            else:
                names[name][1] = True

    addByFilter(names, root)
    
    tree.write(fileName, "UTF-8")
    return len(root.findall('string'))
    
if __name__ == '__main__':
    filterFile = argv[1]
    #标准
    namesInFilter = readNames(filterFile)
    #需修改的文件
    checkFiles = argv[2:]
    for checkFile in checkFiles:
        print checkFile
        length = deleteByFilter(namesInFilter, checkFile)
        print checkFile, ' filter ', len(namesInFilter), 'check ', length
    
