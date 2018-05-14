import re
a="中国人"
if not a.isdigit():
    if(not re.match(r'[a-zA-Z]+',a)):
        print(a)