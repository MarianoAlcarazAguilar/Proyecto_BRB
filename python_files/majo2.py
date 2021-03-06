import re

def _callback(matches):
    id = matches.group(1)
    try:
        return unichr(int(id))
    except:
        return id

def decode_unicode_references(data):
    return re.sub("&#(\d+)(;|(?=\s))", _callback, data)


for element in relevant:
    x = decode_unicode_references(element)
    x = re.findall("var .* = \'(.*)\'", x)
    print(x)
    break
