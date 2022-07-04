import re
from GUID import GuidConverter


class MdzGuidConverter:
    """

    """

    def __init__(self, guid_str: str) -> None:
        """

        :param guid:
        """
        self.__guid_object = MdzGuidConverter.mdz_guid_parser(guid_str)
        if len(self.__guid_object) != 2:
            raise UnboundLocalError("The guid object must contain only one entry.")

    def get_guid_name(self) -> str:
        """

        :return:
        """
        return self.get_correct_guid_macro_name(self.get_macro_guid_name('g'))
        # raise NotImplementedError()

    def get_guid_value(self) -> str:
        """

        :return:
        """
        # return str(uuid.UUID(self.__guid_object["guid"]))
        return self.__guid_object["guid"]
        # raise NotImplementedError()

    def _get_list_of_guid_sub_names(self, guid_name: str) -> list:
        """

        :param guid_name:
        :return:
        """
        list_of_macro_names = list()
        temp_string = ""
        for c in guid_name:
            if c.isupper():
                if temp_string:
                    list_of_macro_names.append(temp_string)
                    temp_string = ""
            temp_string += c
        return list_of_macro_names

    def get_macro_guid_name(self, predicate: str) -> str:
        """

        :return:
        """
        p = re.compile(predicate + r'(.+)')
        # for key in self.__guid_object:
            # if key == "name":
                # m1 = p.search(self.__guid_object[key])
        m1 = p.search(self.__guid_object["name"])
        if m1 is None:
            raise NameError("Error parsing string containing name of guid.")
        return self._get_list_of_guid_sub_names(m1[1])

    def get_correct_guid_macro_name(self, name_strings: list) -> str:
        """

        :param name_strings:
        :return:
        """
        temp_string = ""
        for part in name_strings:
            temp_string += part.upper() + '_'
        return temp_string[:-1]

    @classmethod
    def mdz_guid_parser(cls, guid: str) -> dict:
        """

        :param guid:
        :return:
        """
        p1 = re.compile(r'\s*' +
                       r'([a-zA-Z]+)' +
                       r'\s+=\s+' +
                       r'(' +
                       r'{' +
                       r'\s*0[xX]\w\w\w\w\w\w\w\w,'
                       r'\s*0[xX]\w\w\w\w,' +
                       r'\s*0[xX]\w\w\w\w,' +
                       r'\s*'
                       r'{' +
                       r'\s*0[xX]\w\w?,' +
                       r'\s*0[xX]\w\w?,' +
                       r'\s*0[xX]\w\w?,' 
                       r'\s*0[xX]\w\w?,' +
                       r'\s*0[xX]\w\w?,' +
                       r'\s*0[xX]\w\w?,' +
                       r'\s*0[xX]\w\w?,' +
                       r'\s*0[xX]\w\w?' +
                       r'\s*' +
                       r'}' +
                       r'\s*' +
                       r'}' +
                       r')'
                       )

        p = re.compile(r'\s*' +
                       r'([a-zA-Z]+)' +
                       r'\s+=\s+' +
                       r'(' +
                       r'{' +
                       r'\s*0[xX][0-9a-fA-F]{8},' +
                       r'\s*0[xX][0-9a-fA-F]{4},' +
                       r'\s*0[xX][0-9a-fA-F]{4},' +
                       r'\s*'
                       r'{' +
                       r'\s*0[xX][0-9a-fA-F][0-9a-fA-F]?,' +
                       r'\s*0[xX][0-9a-fA-F][0-9a-fA-F]?,' +
                       r'\s*0[xX][0-9a-fA-F][0-9a-fA-F]?,' +
                       r'\s*0[xX][0-9a-fA-F][0-9a-fA-F]?,' +
                       r'\s*0[xX][0-9a-fA-F][0-9a-fA-F]?,' +
                       r'\s*0[xX][0-9a-fA-F][0-9a-fA-F]?,' +
                       r'\s*0[xX][0-9a-fA-F][0-9a-fA-F]?,' +
                       r'\s*0[xX][0-9a-fA-F][0-9a-fA-F]?' +
                       r'\s*' +
                       r'}' +
                       r'\s*' +
                       r'}' +
                       r')'
                       )

        m1 = p.search(guid)
        if m1 is None:
            raise NotImplementedError("Error parsing string containing guid.")
        return dict(name=m1[1], guid=m1[2])


class FormaterMdzGuidConverter(MdzGuidConverter):
    """

    """

    def __init__(self, guid_str: str):
        """

        :param guid_str:
        """
        super().__init__(guid_str)


if __name__ == '__main__':
    guid_string = "gEfiSimpleTextInputProtocolGuid = {0x387477c1, 0x69c7, 0x11d2, {0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b}}"
    guid_object = MdzGuidConverter.mdz_guid_parser(
        "gEfiSimpleTextIinputProtocolGuid" +
        " = " +
        "{0x387477c1,  0x69c7, 0x11d2, {0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b}}"
    )
    print(guid_object)

    guid = FormaterMdzGuidConverter(guid_string)
    guid_list = guid.get_macro_guid_name('g')
    print(guid_list)
    guid_temp = guid.get_correct_guid_macro_name(guid.get_macro_guid_name('g'))
    print(guid_temp)
    uuid_object = guid.get_guid_value()
    print(uuid_object)
    guid_converter = GuidConverter(uuid_object)
    print(guid_converter.get_guid_as_int())
    print("c1777438c769d2118e3900a0c969723b")
    # print("Group 0: Value:  {0}; Length: {1}; Type:   {2}".format(m1.group(0), len(m1.group(0)), type(m1.group(0))))
    # print("Group 1: Value:  {0}; Length: {1}; Type:   {2}".format(m1.group(1), len(m1.group(1)), type(m1.group(1))))
    # print("Group 2: Value:  {0}; Length: {1}; Type:   {2}".format(m1.group(2), len(m1.group(2)), type(m1.group(2))))
    # print("Group 2: ", M1.group(2))
    with open("./APMDZ_M526-E3_GUIDS.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                mdz_formater = FormaterMdzGuidConverter(line)
            except NotImplementedError:
                continue
            temp_string = "0x" + GuidConverter(mdz_formater.get_guid_value()).get_guid_as_int()
            temp_string += '\N{TAB}'
            temp_string += '(' + mdz_formater.get_correct_guid_macro_name(mdz_formater.get_macro_guid_name('g')) + ')' print(temp_string)
