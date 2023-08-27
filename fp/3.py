from pymonad.tools import curry


@curry(2)
def tag(tagname, value):
    return f'<{tagname}>{value}</{tagname}>'


bold = tag('b')
italic = tag('i')

print(bold('name'))
print(italic('surname'))


@curry(3)
def tag2(tagname, attr, value):
    tag_attr = ''
    if attr:
        for key,value in attr.items():
            tag_attr += f' {key}="{value}"'
    return f'<{tagname}{tag_attr}>{value}</{tagname}>'


li = tag2('li', {'class': 'list-group'})
print(li('middle_name'))
