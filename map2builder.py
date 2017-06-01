import re
import sys


template = 'public void set$1( $1){' \
           'mConfig.put(AliuserConstants.UIConfig.$0, $1);' \
           '}'
def to_camel_case(ks):
    ns = []
    for key in ks:
        parts = key.split('_')
        lowers = list(map(lambda s: s.lower().capitalize(), parts))
        lowers[0] = lowers[0].lower()
        ns.append((key, ''.join(lowers)))
    return ns


def mock_function(k):
    func = template.replace('$1', k[1])
    func = func.replace("$0", k[0])
    print(func)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('error input')

    # 输入文件
    inf = sys.argv[1]

    key_file = open(inf, encoding='utf-8')
    lines = key_file.readlines()

    keys = []
    p = re.compile(r'([A-Z_]+)\s=')

    for line in lines:
        if line.startswith('public static final String '):
            m = p.search(line)
            if m:
                keys.append(m.group(1))

    pairs = to_camel_case(keys)
    for pair in pairs:
        mock_function(pair)
