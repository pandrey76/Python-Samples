
def beautiful_soap_4__sample():
    """

    :return:
    """
    from bs4 import BeautifulSoup

    json_str_1 = '{"action": "block_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }'
    html_str_1 = '<div>' + json_str_1 + '</div>'

    soup = BeautifulSoup(html_str_1, 'html.parser')

    print("soup.div:             ", soup.div)
    # <div>{"action": "block_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }</div>

    print("soup.div.name:        ", soup.div.name)
    # div

    print("soup.div.string:      ", soup.div.string)
    # {"action": "block_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }

    print("soup.div.parent.name: ", soup.div.parent.name)
    # [document]

    print("soup.contents:    ", soup.contents)
    # [<div>{"action": "block_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }</div>]

    print("len(soup.contents):   ", len(soup.contents))
    # 1

    print("soup.contents[0]: ", soup.contents[0])
    # <div>{"action": "block_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }</div>

    print("soup.contents[0].contents:   ", soup.contents[0].contents)
    # ['{"action": "block_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }']

    print("soup.contents[0].name:   ", soup.contents[0].name)
    # div

    print("soup.contents[0].contents[0]:   ", soup.contents[0].contents[0])
    # {"action": "block_devices", "data": { "devices": ["Name1", "Name2", "default_name", "i7"] } }

    i = 0
    for child in soup.contents[0].children:
        print("soup.head.contents[{1}].children: {0}".format(child, i))
        # {"action": "block_devices", "data": {"devices": ["Name1", "Name2", "default_name", "i7"]}}
        i = i + 1


# text.contents
# # AttributeError: У объекта 'NavigableString' нет атрибута 'contents'
# Вместо того, чтобы получать дочерние элементы в виде списка, вы можете перебирать их с помощью генератора .children:
#
# for child in title_tag.children:
#     print(child)
# # The Dormouse's story


if __name__ == "__main__":
    beautiful_soap_4__sample()





