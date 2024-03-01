import re

def solution(files):
    answer = []
    l = [{'ORI': None, 'HEAD':None, 'NUMBER': None, 'TAIL': None} for _ in range(len(files))]
    pattern = re.compile(r'([a-zA-Z.\-\s]*)([0-9]{0,5})(.*)')
    for idx, file in enumerate(files):
        l[idx]['ORI'] = file
        file = pattern.match(file)
        l[idx]['HEAD'] = file.group(1).lower()
        l[idx]['NUMBER'] = int(file.group(2))
        l[idx]['TAIL'] = file.group(3)
    
    l = sorted(l, key = lambda x: (x['HEAD'], x['NUMBER']))
    
    return [res['ORI'] for res in l]
